from typing import Any

from ipywidgets import HTMLMath, Layout, Tab, VBox

from ..unit import EqWithUnit


class EquationShowWidget(VBox):  # type: ignore
  def __init__(self, **kwargs: dict[str, Any]):
    super().__init__(**kwargs)
    HTMLMath()

  def add(self, eq: EqWithUnit) -> None:
    self.children += (HTMLMath(f'${eq._repr_latex_()}$'),)


class EquationWidget(Tab):  # type: ignore
  equations: list[EqWithUnit]
  child: EquationShowWidget

  def __init__(self, **kwargs: dict[str, Any]) -> None:
    self.equations = []
    self.child = EquationShowWidget(layout=Layout(width='100%'))
    super().__init__([self.child], layout=Layout(width='95%'), **kwargs)
    self.set_title(0, '関係式')

  def add(self, eq: EqWithUnit) -> None:
    if eq in self.equations:
      raise ValueError(f'Equation {eq} already exists.')
    self.equations.append(eq)
    self.child.add(eq)
