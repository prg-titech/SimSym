from typing import Callable

from ipywidgets import Button, HBox, Layout, Text


class ObjGenerateWidget(HBox):  # type: ignore
  def __init__(self) -> None:
    text_input = Text(placeholder='名前を入力', layout=Layout(width='90px'))
    self.text_input = text_input
    button = Button(description='物体追加', layout=Layout(width='80px'))
    self.button = button
    super().__init__(children=[text_input, button])

  def set_callback(self, callback: Callable[[str], None]) -> None:
    self.button.on_click(lambda _: callback(self.text_input.value))

  def clear(self) -> None:
    self.text_input.value = ''
