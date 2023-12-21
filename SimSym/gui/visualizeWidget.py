from typing import Any

import numpy as np
from IPython import display
from ipywidgets import Checkbox, Output, VBox, interactive_output
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation

from SimSym.unit import ExprWithUnit


class VisualizeWidget(VBox):  # type: ignore
  graph: Output
  x_expr: ExprWithUnit | None
  y_expr: ExprWithUnit | None

  def __init__(self, **kwargs: dict[str, Any]) -> None:
    self.x_expr = None
    self.y_expr = None

    self.dummy_checkbox = Checkbox(description='更新用のダミーのチェックボックス')
    self.graph = interactive_output(self.draw, {
        'dummy': self.dummy_checkbox,
    })

    super().__init__([self.graph], **kwargs)
    # self.set_title(0, 'グラフ')

  def update(self) -> None:
    self.dummy_checkbox.value = not self.dummy_checkbox.value

  def draw(self, dummy: bool, *args: Any, **kwargs: dict[str, Any]) -> None:
    fig = plt.figure()
    # データの作成
    frames = []
    num_frames = 100
    for i in range(num_frames):
      rad = 2 * np.pi * i * 2 / num_frames
      x = np.cos(rad)
      y = np.sin(rad)
      frame = plt.scatter(x, y, color='blue')
      frames.append([frame])
    ani = ArtistAnimation(fig, frames, interval=100)
    html = display.HTML(ani.to_jshtml())  # type: ignore
    display.display(html)  # type: ignore
    plt.close()

  def set_x_expr(self, expr: ExprWithUnit) -> None:
    self.x_expr = expr
    self.update()

  def set_y_expr(self, expr: ExprWithUnit) -> None:
    self.y_expr = expr
    self.update()
