from __future__ import annotations

from typing import TypeVar

from PhysicalQuantities import q
from PhysicalQuantities.quantity import PhysicalQuantity
from sympy import Symbol, latex
from sympy import nsimplify as _nsimplify
from sympy.core.expr import Expr

T = TypeVar('T')


def nsimplify(expr: Expr) -> Expr:
  """
  Simplify a sympy expression.
  """
  return _nsimplify(expr)  # type: ignore


class ExprWithUnit:
  """
  Expr with a unit.
  """
  expr: Expr
  pq: PhysicalQuantity

  def __init__(self, expr: Expr | str, pq: PhysicalQuantity | str) -> None:
    if isinstance(expr, str):
      self.expr = Symbol(expr)  # type: ignore
    else:
      self.expr = expr

    if isinstance(pq, str):
      try:
        self.pq = q[pq]
      except KeyError as e:
        raise e
    else:
      self.pq = pq

  def __str__(self) -> str:
    return f'{str(nsimplify(self.expr))} {str(self.pq.unit)}'

  def __repr__(self) -> str:
    return self.__str__()

  def _repr_latex_(self) -> str:
    """
    Return latex representation for IPython notebook
    """
    return ''.join([
        '$',
        latex(nsimplify(self.expr)),
        r'~\mathrm{[',
        self.pq.unit._repr_latex_(),
        ']}$',
    ])

  def __add__(self, other: ExprWithUnit) -> ExprWithUnit:
    return ExprWithUnit(self.expr + other.expr, self.pq + other.pq)

  def __sub__(self, other: ExprWithUnit) -> ExprWithUnit:
    return ExprWithUnit(self.expr - other.expr, self.pq - other.pq)

  def __mul__(self, other: ExprWithUnit | float) -> ExprWithUnit:
    if isinstance(other, float):
      return ExprWithUnit(self.expr * other, self.pq)
    return ExprWithUnit(self.expr * other.expr, self.pq * other.pq)

  def __rmul__(self, other: ExprWithUnit | float) -> ExprWithUnit:
    if isinstance(other, float):
      return ExprWithUnit(self.expr * other, self.pq)
    return ExprWithUnit(self.expr * other.expr, self.pq * other.pq)

  def __truediv__(self, other: ExprWithUnit) -> ExprWithUnit:
    return ExprWithUnit(self.expr / other.expr, self.pq / other.pq)

  def __pow__(self, other: float) -> ExprWithUnit:
    return ExprWithUnit(self.expr ** other, self.pq ** other)
