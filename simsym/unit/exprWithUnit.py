from __future__ import annotations

from typing import Any

from PhysicalQuantities import q
from PhysicalQuantities.quantity import PhysicalQuantity
from sympy import Symbol, latex
from sympy import nsimplify as _nsimplify
from sympy.core.expr import Expr


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
  pq: PhysicalQuantity | float

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
    if isinstance(self.pq, PhysicalQuantity):
      return f'{str(nsimplify(self.expr))} {str(self.pq.unit)}'
    else:
      return f'{str(nsimplify(self.expr))} [1]'

  def __repr__(self) -> str:
    return self.__str__()

  def _repr_latex_(self) -> str:
    """
    Return latex representation for IPython notebook
    """
    unit_repr = self.pq.unit._repr_latex_() if isinstance(self.pq, PhysicalQuantity) else '1'
    return ''.join([
        '$',
        latex(nsimplify(self.expr)),
        r'~\mathrm{[',
        unit_repr,
        ']}$',
    ])

  def __add__(self, other: ExprWithUnit) -> ExprWithUnit:
    return ExprWithUnit(self.expr + other.expr, self.pq + other.pq)

  def __sub__(self, other: ExprWithUnit) -> ExprWithUnit:
    return ExprWithUnit(self.expr - other.expr, self.pq - other.pq)

  def __mul__(self, other: ExprWithUnit | Any) -> ExprWithUnit:
    if isinstance(other, ExprWithUnit):
      return ExprWithUnit(self.expr * other.expr, self.pq * other.pq)
    else:
      return ExprWithUnit(self.expr * other, self.pq)

  def __rmul__(self, other: Any) -> ExprWithUnit:
    return ExprWithUnit(self.expr * other, self.pq)

  # TODO: ExprWithUnit 以外も実装
  def __truediv__(self, other: ExprWithUnit) -> ExprWithUnit:
    return ExprWithUnit(self.expr / other.expr, self.pq / other.pq)

  def __pow__(self, other: Any) -> ExprWithUnit:
    return ExprWithUnit(self.expr ** other, self.pq ** other)
