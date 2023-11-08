from typing import Any

from ipywidgets import HBox, HTMLMath, Layout, Tab

from SimSym.model import Obj


class ObjVarShowWidget(HBox):  # type: ignore
  variables: tuple[HTMLMath, ...]

  def __init__(self, obj: Obj, **kwargs: dict[str, Any]):
    variables: list[HTMLMath] = []
    for variable in obj.variables.values():
      variables.append(HTMLMath(variable._repr_latex_()))
    self.variables = tuple(variables)
    super().__init__(self.variables, **kwargs)
    self.add_class('flexgrid')


class ObjVarWidget(Tab):  # type: ignore
  objs: list[Obj]
  children: tuple[ObjVarShowWidget, ...]

  def __init__(self, **kwargs: dict[str, Any]) -> None:
    self.objs = []
    self.children = tuple()
    super().__init__(self.children, layout=Layout(width='95%'), **kwargs)

  def add_object(self, obj: Obj) -> None:
    if obj in self.objs:
      raise ValueError(f'Object {obj.name} already exists.')
    self.objs.append(obj)
    tab = ObjVarShowWidget(obj, layout=Layout(width='100%'))
    self.children = (*self.children, tab)
    self.set_title(len(self.children)-1, obj.name)
