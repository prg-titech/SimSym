from typing import Any

from ipywidgets import HTMLMath, Layout, Tab, VBox

from ..model import EquationHolder
from ..unit import EqWithUnit


class EquationShowWidget(VBox):  # type: ignore
  def __init__(self, **kwargs: dict[str, Any]):
    super().__init__(**kwargs)
    HTMLMath()

  def add(self, eq: EqWithUnit) -> None:
    self.children += (HTMLMath(f'${eq._repr_latex_()}$'),)


class EquationWidget(Tab):  # type: ignore
  child: EquationShowWidget
  equationHolder: EquationHolder

  def __init__(self, equationHolder: EquationHolder, **kwargs: dict[str, Any]) -> None:
    self.equationHolder = equationHolder
    self.child = EquationShowWidget(layout=Layout(width='100%'))
    super().__init__([self.child], layout=Layout(width='95%'), **kwargs)
    self.set_title(0, '関係式')

  def add(self, eq: EqWithUnit) -> None:
    self.equationHolder.add(eq)
    self.child.add(eq)
