from sympy import Expr
from sympy import nsimplify as _nsimplify


def nsimplify(expr: Expr) -> Expr:
  """
  Simplify a sympy expression.
  """
  return _nsimplify(expr)  # type: ignore
