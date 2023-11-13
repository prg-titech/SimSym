from __future__ import annotations

from ..utility import alert


class VariableHolder:
  from ..unit import ExprWithUnit
  """
  A class that holds variables.
  **singleton**
  """
  _instance: VariableHolder
  variables: dict[str, ExprWithUnit]

  def __new__(cls) -> VariableHolder:
    if not hasattr(cls, '_instance'):
      cls._instance = super().__new__(cls)
      cls._instance.variables = {}
    return cls._instance

  def add(self, variable: ExprWithUnit) -> None:
    if str(variable) in self.variables.keys():
      alert(f"変数 {variable} はすでに存在します。")
      raise ValueError(f'Variable {variable} already exists.')
    self.variables[str(variable)] = variable

  def get(self, name: str) -> ExprWithUnit:
    if name not in self.variables:
      alert(f"変数 {name} は存在しません。")
      raise ValueError(f'Variable {name} does not exist.')
    return self.variables[name]
