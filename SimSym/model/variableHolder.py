from __future__ import annotations

from ..exception import VarAlreadyDefinedException, VarNotDefinedException
from ..unit.exprWithUnit import ExprWithUnit
from ..utility import alert_exception


class VariableHolder:
  """
  A class that holds variables.
  """
  variables: dict[str, ExprWithUnit]

  def __init__(self) -> None:
    self.variables = {}

  def add(self, variable: ExprWithUnit) -> None:
    if variable.to_key in self.variables.keys():
      alert_exception(VarAlreadyDefinedException(variable.to_key))
    self.variables[variable.to_key] = variable

  def get(self, name: str) -> ExprWithUnit:
    if name not in self.variables.keys():
      alert_exception(VarNotDefinedException(name))
    return self.variables[name]
