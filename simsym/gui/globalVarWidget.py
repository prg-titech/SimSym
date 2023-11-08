from typing import Any

from ipywidgets import HBox, HTMLMath, Layout, Tab

from ..unit import ExprWithUnit


class GlobalVarShowWidget(HBox):  # type: ignore
  variables: tuple[HTMLMath, ...]

  def __init__(self, vars: list[ExprWithUnit], **kwargs: dict[str, Any]):
    variables: list[HTMLMath] = []
    for variable in vars:
      variables.append(HTMLMath(value=variable._repr_latex_()))
    self.variables = tuple(variables)
    super().__init__(self.variables, **kwargs)
    self.add_class('flexgrid')


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
