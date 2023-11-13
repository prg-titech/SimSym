from typing import Any

from ipywidgets import HBox, HTMLMath, Layout, Tab

from ..model import VariableHolder
from ..unit import ExprWithUnit


class GlobalVarShowWidget(HBox):  # type: ignore
  def __init__(self, vars: list[ExprWithUnit], **kwargs: dict[str, Any]):
    variables: list[HTMLMath] = []
    super().__init__(tuple(variables), **kwargs)
    self.add_class('flexgrid')

  def add(self, expr: ExprWithUnit) -> None:
    self.children += (HTMLMath(f'${expr._repr_latex_()}$'),)


class GlobalVarWidget(Tab):  # type: ignore
  vars: list[ExprWithUnit]
  variableHolder: VariableHolder
  child: GlobalVarShowWidget

  def __init__(self, variableHolder: VariableHolder, **kwargs: dict[str, Any]) -> None:
    self.variableHolder = variableHolder
    self.vars = []
    self.child = GlobalVarShowWidget(self.vars, layout=Layout(width='100%'))
    super().__init__([self.child], layout=Layout(width='95%'), **kwargs)
    self.set_title(0, '変数')

    self.add(ExprWithUnit('t', 's'))
    self.add(ExprWithUnit('g', 'm/s/s'))

  def add(self, expr: ExprWithUnit) -> None:
    self.variableHolder.add(expr)
    self.vars.append(expr)
    self.child.add(expr)
