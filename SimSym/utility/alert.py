from IPython.display import Javascript, display


def alert(msg: str) -> None:
  display(Javascript(f'alert("{msg}")'))  # type: ignore


def alert_exception(e: Exception) -> None:
  alert(str(e))
  raise e
