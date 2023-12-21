from typing import Any

from ipywidgets import Layout, Tab, VBox

from SimSym.gui.axisSetWidget import AxesSetWidget

from ..model import EquationHolder, VariableHolder
from .visualizeWidget import VisualizeWidget


class ObservePane(Tab):  # type: ignore
  variable_holder: VariableHolder
  equation_holder: EquationHolder
  axes_set_widget: AxesSetWidget

  def __init__(
      self,
      variable_holder: VariableHolder | None = None,
      equation_holder: EquationHolder | None = None,
      visualize_widget: VisualizeWidget | None = None,
      **kwargs: dict[str, Any]
  ) -> None:
    self.variable_holder = variable_holder or VariableHolder()
    self.equation_holder = equation_holder or EquationHolder()
    self.visualize_widget = visualize_widget or VisualizeWidget()

    self.axes_set_widget = AxesSetWidget(self.variable_holder)
    self.axes_set_widget.x_expr_input.set_callback(self.visualize_widget.set_x_expr)
    self.axes_set_widget.y_expr_input.set_callback(self.visualize_widget.set_y_expr)

    super().__init__(
        children=[VBox([
            self.visualize_widget,
            self.axes_set_widget,
        ])],
        layout=Layout(width='45%'),
        **kwargs,
    )
    self.set_title(0, '観測ペイン')
