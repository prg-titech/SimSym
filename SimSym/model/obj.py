from ..unit import ExprWithUnit
from .variableHolder import VariableHolder


class Obj:
  name: str
  variables: dict[str, ExprWithUnit]
  variableHolder: VariableHolder

  def __init__(self, name: str, variableHolder: VariableHolder) -> None:
    self.name = name
    self.variableHolder = variableHolder
    self.variables = generate_init_variables(name)
    for variable in self.variables.values():
      self.variableHolder.add(variable)

  def __repr__(self) -> str:
    return f'Obj({self.name})'

  def __eq__(self, other: object) -> bool:
    if isinstance(other, Obj):
      return self.name == other.name
    else:
      return False

  def add_variable(self, variable: ExprWithUnit) -> None:
    self.variableHolder.add(variable)
    self.variables[str(variable)] = variable


def generate_init_variables(name: str) -> dict[str, ExprWithUnit]:
  variables: dict[str, ExprWithUnit] = {}
  x = ExprWithUnit(f'x_{name}', 'm')
  variables[str(x)] = x
  y = ExprWithUnit(f'y_{name}', 'm')
  variables[str(y)] = y
  v_x = ExprWithUnit(f'v_{{{name}x}}', 'm/s')
  variables[str(v_x)] = v_x
  v_y = ExprWithUnit(f'v_{{{name}y}}', 'm/s')
  variables[str(v_y)] = v_y
  return variables
