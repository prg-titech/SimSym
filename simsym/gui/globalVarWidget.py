from typing import Any

from ipywidgets import HBox, HTMLMath, Layout, Tab

from ..unit import ExprWithUnit


class GlobalVarShowWidget(HBox):  # type: ignore
  def __init__(self, vars: list[ExprWithUnit], **kwargs: dict[str, Any]):
    variables: list[HTMLMath] = []
    for variable in vars:
      variables.append(HTMLMath(f'${variable._repr_latex_()}$'))
    super().__init__(tuple(variables), **kwargs)
    self.add_class('flexgrid')

  def add(self, expr: ExprWithUnit) -> None:
    self.children += (HTMLMath(f'${expr._repr_latex_()}$'),)


class GlobalVarWidget(Tab):  # type: ignore
  vars: list[ExprWithUnit]
  child: GlobalVarShowWidget

  def __init__(self, **kwargs: dict[str, Any]) -> None:
    self.vars = []
    self.vars.append(ExprWithUnit('t', 's'))
    self.vars.append(ExprWithUnit('g', 'm/s/s'))
    self.child = GlobalVarShowWidget(self.vars, layout=Layout(width='100%'))
    super().__init__([self.child], layout=Layout(width='95%'), **kwargs)
    self.set_title(0, '変数')

  def add(self, expr: ExprWithUnit) -> None:
    if expr in self.vars:
      raise ValueError(f'Variable {expr} already exists.')
    self.vars.append(expr)
    self.child.add(expr)
