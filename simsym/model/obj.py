from SimSym.unit import ExprWithUnit


class Obj:
  name: str
  variables: dict[str, ExprWithUnit]

  def __init__(self, name: str) -> None:
    self.name = name
    self.variables = generate_init_variables(name)

  def __repr__(self) -> str:
    return f'Obj({self.name})'

  def __eq__(self, other: object) -> bool:
    if isinstance(other, Obj):
      return self.name == other.name
    else:
      return False


def generate_init_variables(name: str) -> dict[str, ExprWithUnit]:
  variables: dict[str, ExprWithUnit] = {}
  variables[f'x_{name}'] = ExprWithUnit(f'x_{name}', 'm')
  variables[f'y_{name}'] = ExprWithUnit(f'y_{name}', 'm')
  variables[f'v_{{{name}x}}'] = ExprWithUnit(f'v_{{{name}x}}', 'm/s')
  variables[f'v_{{{name}y}}'] = ExprWithUnit(f'v_{{{name}y}}', 'm/s')
  return variables
