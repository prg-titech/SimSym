from IPython.display import Javascript, display


def alert(msg: str) -> None:
  display(Javascript(f'alert("{msg}")'))  # type: ignore
