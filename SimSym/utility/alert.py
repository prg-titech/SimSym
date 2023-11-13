from __future__ import annotations

from IPython.display import Javascript, display
from ipywidgets import Output


class AlertOutput(object):
  """
  singleton
  """
  _instance: AlertOutput
  out: Output

  def __new__(cls) -> AlertOutput:
    if not hasattr(cls, '_instance'):
      cls._instance = super().__new__(cls)
      cls.out = Output()
    return cls._instance


@AlertOutput().out.capture(clear_output=True)  # type: ignore
def alert(msg: str) -> None:
  display(Javascript(f'alert("{msg}")'))  # type: ignore


def alert_exception(e: Exception) -> None:
  alert(str(e))
  raise e
