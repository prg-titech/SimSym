from __future__ import annotations

from ..unit import EqWithUnit
from ..utility import alert_exception


class EquationHolder:
  """
  A class that holds equations.
  """
  _instance: EquationHolder
  equations: dict[str, EqWithUnit]

  def __init__(self) -> None:
    self.equations = {}

  def add(self, eq: EqWithUnit) -> None:
    if str(eq) in self.equations.keys():
      alert_exception(ValueError(f'関係式 {eq} はすでに存在します。'))
    self.equations[str(eq)] = eq
