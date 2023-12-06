from typing import Any

from ipywidgets import Layout, Tab, VBox

from ..model import EquationHolder, VariableHolder


class ObservePane(Tab):  # type: ignore
  variable_holder: VariableHolder
  equation_holder: EquationHolder

  def __init__(
      self,
      variable_holder: VariableHolder | None = None,
      equation_holder: EquationHolder | None = None,
      **kwargs: dict[str, Any]
  ) -> None:
    self.variable_holder = variable_holder or VariableHolder()
    self.equation_holder = equation_holder or EquationHolder()

    super().__init__(
        children=[VBox([

        ])],
        layout=Layout(width='45%'),
        **kwargs,
    )
    self.set_title(0, '観測ペイン')
