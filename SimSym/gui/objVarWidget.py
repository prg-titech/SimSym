from typing import Any

from ipywidgets import HBox, HTMLMath, Layout, Tab

from ..exception import ObjAlreadyDefinedException
from ..model import Obj, VariableHolder
from ..unit import ExprWithUnit
from ..utility import alert_exception


class ObjVarShowWidget(HBox):  # type: ignore
  obj: Obj

  def __init__(self, obj: Obj, **kwargs: dict[str, Any]):
    self.obj = obj
    variables: list[HTMLMath] = []
    for variable in obj.variables.values():
      variables.append(HTMLMath(f'${variable._repr_latex_()}$'))
    super().__init__(variables, **kwargs)
    self.add_class('flexgrid')

  def add(self, variable: ExprWithUnit) -> None:
    self.obj.add_variable(variable)
    self.children += (HTMLMath(f'${variable._repr_latex_()}$'),)


class ObjVarWidget(Tab):  # type: ignore
  objs: dict[str, Obj]
  variableHolder: VariableHolder
  children: tuple[ObjVarShowWidget, ...]

  def __init__(self, variableHolder: VariableHolder, **kwargs: dict[str, Any]) -> None:
    self.variableHolder = variableHolder
    self.objs = {}
    self.children = tuple()
    super().__init__(self.children, layout=Layout(width='95%'), **kwargs)

  def add_object(self, obj: Obj) -> None:
    self.objs[obj.name] = obj
    tab = ObjVarShowWidget(obj, layout=Layout(width='100%'))
    self.children += (tab,)
    self.set_title(len(self.children) - 1, obj.name)

  def add_object_by_name(self, name: str) -> None:
    if name in self.objs.keys():
      alert_exception(ObjAlreadyDefinedException(name))
    self.add_object(Obj(name, self.variableHolder))
