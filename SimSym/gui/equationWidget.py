from typing import Any

from ipywidgets import Button, HBox, HTMLMath, Layout, Tab, Text, VBox

from ..exception import IllegalEquationException
from ..model import EquationHolder, VariableHolder
from ..unit import EqWithUnit
from ..utility.alert import alert_exception
from ..utility.parseWithUnit import parse_with_unit


class EquationShowWidget(VBox):  # type: ignore
  def __init__(self, **kwargs: dict[str, Any]):
    super().__init__(**kwargs)
    HTMLMath()

  def add(self, eq: EqWithUnit) -> None:
    self.children += (HTMLMath(f'${eq._repr_latex_()}$'),)


class EquationAddWidget(HBox):  # type: ignore
  def __init__(self, equation_holder: EquationHolder, **kwargs: dict[str, Any]) -> None:
    self.text_input = Text(placeholder='関係式', layout=Layout(width='200px'))
    self.button = Button(description='追加', layout=Layout(width='80px'))
    super().__init__(children=[self.text_input, self.button], **kwargs)
    self.equation_holder = equation_holder

  def clear(self) -> None:
    self.text_input.value = ''


class EquationWidget(Tab):  # type: ignore
  show_widget: EquationShowWidget
  add_widget: EquationAddWidget
  equation_holder: EquationHolder

  def __init__(self, equation_holder: EquationHolder, **kwargs: dict[str, Any]) -> None:
    self.equation_holder = equation_holder
    self.show_widget = EquationShowWidget(layout=Layout(width='100%'))
    self.add_widget = EquationAddWidget(self.equation_holder)
    vbox = VBox([self.show_widget, self.add_widget])
    super().__init__([vbox], layout=Layout(width='95%'), **kwargs)
    self.set_title(0, '関係式')

  def add(self, eq: EqWithUnit) -> None:
    self.equation_holder.add(eq)
    self.show_widget.add(eq)

  def set_callback(self, vh: VariableHolder) -> None:
    def callback(_: Any) -> None:
      splitted = self.add_widget.text_input.value.split('=')
      if len(splitted) != 2:
        alert_exception(IllegalEquationException())
      lhs_text, rhs_text = splitted
      try:
        lhs = parse_with_unit(lhs_text, vh)
        rhs = parse_with_unit(rhs_text, vh)
        eq = EqWithUnit(lhs, rhs)
        self.add(eq)
        self.add_widget.clear()
      except Exception as e:
        alert_exception(e)
    self.add_widget.button.on_click(callback)
