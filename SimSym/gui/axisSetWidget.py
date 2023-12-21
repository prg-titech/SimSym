from typing import Any, Callable

from ipywidgets import Button, HBox, Label, Layout, Text, VBox

from SimSym.model.variableHolder import VariableHolder
from SimSym.unit import ExprWithUnit
from SimSym.utility.alert import alert_exception
from SimSym.utility.parseWithUnit import parse_with_unit


class ExprInput(HBox):  # type: ignore
  variable_holder: VariableHolder
  text_input: Text
  placeholder: str
  button: Button
  current_var: ExprWithUnit | None

  def __init__(
      self,
      variable_holder: VariableHolder,
      placeholder: str,
      **kwargs: dict[str, Any]
  ) -> None:
    self.variable_holder = variable_holder
    self.placeholder = placeholder
    self.text_input = Text(placeholder=placeholder, layout=Layout(width='40%'))
    self.button = Button(description='変更', layout=Layout(width='20%'))
    self.current_var = None
    label_text = f'現在の{placeholder}: なし'
    self.label = Label(label_text, layout=Layout(width='40%'))

    super().__init__(children=(
        self.text_input,
        self.button,
        self.label,
    ), **kwargs)

  def set_callback(self, callback: Callable[[ExprWithUnit], None]) -> None:
    self.button.on_click(lambda _: self.on_button_click(callback))

  def on_button_click(self, callback: Callable[[ExprWithUnit], None]) -> None:
    if self.text_input.value == '':
      return
    try:
      expr = parse_with_unit(self.text_input.value, self.variable_holder)
    except Exception as e:
      alert_exception(e)
    self.current_var = expr
    callback(expr)
    self.label.value = f'現在の{self.placeholder}: {self.current_var}'
    self.text_input.value = ''


class AxesSetWidget(VBox):  # type: ignore
  variable_holder: VariableHolder
  x_expr_input: ExprInput
  y_expr_input: ExprInput

  def __init__(self, variable_holder: VariableHolder, **kwargs: dict[str, Any]) -> None:
    self.variable_holder = variable_holder
    self.x_expr_input = ExprInput(variable_holder, 'x軸')
    self.y_expr_input = ExprInput(variable_holder, 'y軸')

    super().__init__(children=(self.x_expr_input, self.y_expr_input), **kwargs)
