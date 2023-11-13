from __future__ import annotations

from ..unit import ExprWithUnit
from ..utility import alert


class VariableHolder:
  """
  A class that holds variables.
  """
  variables: dict[str, ExprWithUnit]

  def __init__(self) -> None:
    self.variables = {}

  def add(self, variable: ExprWithUnit) -> None:
    if variable.to_key in self.variables.keys():
      alert(f"変数 {variable} はすでに存在します。")
      raise ValueError(f'Variable {variable} already exists.')
    self.variables[variable.to_key] = variable

  def get(self, name: str) -> ExprWithUnit:
    if name not in self.variables.keys():
      alert(f"変数 {name} は存在しません。")
      raise ValueError(f'Variable {name} does not exist.')
    return self.variables[name]
