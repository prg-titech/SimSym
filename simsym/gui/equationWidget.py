from typing import Any

from ipywidgets import HBox, HTMLMath


class EquationShowWidget(HBox):  # type: ignore
  equations: tuple[HTMLMath, ...]

  def __init__(self, **kwargs: dict[str, Any]):
    super().__init__(**kwargs)
