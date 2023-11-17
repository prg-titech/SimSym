from typing import Any

from ipywidgets import Button, HBox, HTMLMath, Layout, Tab, Text, VBox

from ..exception import EmptyException, ObjAlreadyDefinedException
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


class ObjVarAddWidget(HBox):  # type: ignore
  def __init__(self, variable_holder: VariableHolder, **kwargs: dict[str, Any]) -> None:
    self.text_input = Text(placeholder='変数名', layout=Layout(width='90px'))
    self.unit_input = Text(placeholder='単位', layout=Layout(width='90px'))
    self.button = Button(description='追加', layout=Layout(width='80px'))
    super().__init__(children=[self.text_input, self.unit_input, self.button], **kwargs)
    self.variable_holder = variable_holder

  def clear(self) -> None:
    self.text_input.value = ''
    self.unit_input.value = ''


class ObjVarWidget(Tab):  # type: ignore
  objs: dict[str, Obj]
  variable_holder: VariableHolder
  children: tuple[ObjVarShowWidget, ...]

  def __init__(self, variable_holder: VariableHolder, **kwargs: dict[str, Any]) -> None:
    self.variable_holder = variable_holder
    self.objs = {}
    self.children = tuple()
    super().__init__(self.children, layout=Layout(width='95%'), **kwargs)

  def add_object(self, obj: Obj) -> None:
    self.objs[obj.name] = obj
    show_widget = ObjVarShowWidget(obj, layout=Layout(width='100%'))
    add_widget = ObjVarAddWidget(self.variable_holder)
    self.set_callback(show_widget, add_widget)
    tab = VBox([show_widget, add_widget])
    self.children += (tab,)
    self.set_title(len(self.children) - 1, obj.name)

  def add_object_by_name(self, name: str) -> None:
    if name == '':
      alert_exception(EmptyException('物体名'))
    if name in self.objs.keys():
      alert_exception(ObjAlreadyDefinedException(name))
    self.add_object(Obj(name, self.variable_holder))

  def set_callback(self, show_widget: ObjVarShowWidget, add_widget: ObjVarAddWidget) -> None:
    def callback(_: Any) -> None:
      show_widget.add(ExprWithUnit(add_widget.text_input.value, add_widget.unit_input.value))
      add_widget.clear()
    add_widget.button.on_click(callback)
