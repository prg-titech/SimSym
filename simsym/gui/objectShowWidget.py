from ipywidgets import HBox, Layout


class ObjectShowWidget(HBox):  # type: ignore
  def __init__(self) -> None:
    super().__init__([], layout=Layout(width='100%'))
