from typing import Any

from .objVarWidget import ObjVarWidget

from ipywidgets import Button, HBox, Layout, Text


class ObjGenerateWidget(HBox):  # type: ignore
  def __init__(self) -> None:
    text_input = Text(placeholder='名前を入力', layout=Layout(width='90px'))
    self.text_input = text_input
    button = Button(description='物体追加', layout=Layout(width='80px'))
    self.button = button
    super().__init__(children=[text_input, button])

  def set_callback(self, obj_var_widget: ObjVarWidget) -> None:
    def callback(_: Any) -> None:
      obj_var_widget.add_object_by_name(self.text_input.value)
      self.clear()
    self.button.on_click(callback)

  def clear(self) -> None:
    self.text_input.value = ''
