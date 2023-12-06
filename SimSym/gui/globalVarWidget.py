from typing import Any

from ipywidgets import Button, HBox, HTMLMath, Layout, Tab, Text, VBox

from ..model import VariableHolder
from ..unit import ExprWithUnit


class GlobalVarShowWidget(HBox):  # type: ignore
  def __init__(self, vars: list[ExprWithUnit], **kwargs: dict[str, Any]):
    variables: list[HTMLMath] = []
    super().__init__(tuple(variables), **kwargs)
    self.add_class('flexgrid')

  def add(self, expr: ExprWithUnit) -> None:
    self.children += (HTMLMath(f'${expr._repr_latex_()}$'),)


class GlobalVarAddWidget(HBox):  # type: ignore
  def __init__(self, variable_holder: VariableHolder, **kwargs: dict[str, Any]) -> None:
    self.text_input = Text(placeholder='変数名', layout=Layout(width='90px'))
    self.unit_input = Text(placeholder='単位', layout=Layout(width='90px'))
    self.button = Button(description='追加', layout=Layout(width='80px'))
    super().__init__(children=[self.text_input, self.unit_input, self.button], **kwargs)
    self.variable_holder = variable_holder

  def clear(self) -> None:
    self.text_input.value = ''
    self.unit_input.value = ''


class GlobalVarWidget(Tab):  # type: ignore
  vars: list[ExprWithUnit]
  variable_holder: VariableHolder
  show_widget: GlobalVarShowWidget
  add_widget: GlobalVarAddWidget

  def __init__(self, variable_holder: VariableHolder, **kwargs: dict[str, Any]) -> None:
    self.variable_holder = variable_holder
    self.vars = []
    self.show_widget = GlobalVarShowWidget(self.vars, layout=Layout(width='100%'))
    self.add_widget = GlobalVarAddWidget(self.variable_holder)
    vbox = VBox([self.show_widget, self.add_widget])
    super().__init__([vbox], layout=Layout(width='95%'), **kwargs)
    self.set_title(0, '変数')

    self.add(ExprWithUnit('t', 's'))
    self.add(ExprWithUnit('g', 'm/s/s'))

  def add(self, expr: ExprWithUnit) -> None:
    self.variable_holder.add(expr)
    self.vars.append(expr)
    self.show_widget.add(expr)

  def set_callback(self) -> None:
    def callback(_: Any) -> None:
      self.add(
          ExprWithUnit(
              self.add_widget.text_input.value,
              self.add_widget.unit_input.value))
      self.add_widget.clear()
    self.add_widget.button.on_click(callback)
