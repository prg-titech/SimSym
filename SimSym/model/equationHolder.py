from __future__ import annotations

from ..unit import EqWithUnit
from ..utility import alert


class EquationHolder:
  """
  A class that holds equations.
  **singleton**
  """
  _instance: EquationHolder
  equations: dict[str, EqWithUnit]

  def __init__(self) -> None:
    self.equations = {}

  def add(self, eq: EqWithUnit) -> None:
    if str(eq) in self.equations.keys():
      alert(f'関係式 {eq} はすでに存在します。')
      raise ValueError(f'Equation {eq} already exists.')
    self.equations[str(eq)] = eq
