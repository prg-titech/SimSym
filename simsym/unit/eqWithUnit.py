from sympy import latex

from ..utility import nsimplify
from .exprWithUnit import ExprWithUnit


class EqWithUnit:
  lhs: ExprWithUnit
  rhs: ExprWithUnit

  def __init__(self, lhs: ExprWithUnit, rhs: ExprWithUnit) -> None:
    lhs.pq + rhs.pq
    self.lhs = lhs
    self.rhs = rhs

  def __str__(self) -> str:
    return str(nsimplify(self.lhs.expr))\
        + '='\
        + str(nsimplify(self.rhs.expr))\
        + str(self.lhs.pq)

  def __eq__(self, other: object) -> bool:
    if isinstance(other, EqWithUnit):
      return self.lhs == other.lhs and self.rhs == other.rhs
    else:
      return False

  def __repr__(self) -> str:
    return f'EqWithUnit({repr(self.lhs)}, {repr(self.rhs)})'

  def _repr_latex_(self) -> str:
    lhs_latex: str = latex(nsimplify(self.lhs.expr))
    rhs_latex: str = latex(nsimplify(self.rhs.expr))
    unit_latex: str = self.lhs.pq._repr_latex_()
    return f'{lhs_latex}={rhs_latex}~{unit_latex}'
