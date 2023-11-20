from __future__ import annotations

from typing import Any

from PhysicalQuantities.quantity import PhysicalQuantity
from PhysicalQuantities.unit import PhysicalUnit, UnitError
from sympy import Symbol, latex
from sympy.core.expr import Expr

from ..utility.nsimplify import nsimplify


# PhysicalUnit の _repr_latex_ を上書きする
def _repr_latex_(self: PhysicalUnit) -> str:
  """ Return LaTeX representation for IPython notebook

  Returns
  -------
  str
      Unit as LaTeX string
  """
  num = ''
  denom = ''
  for unit in self.names.keys():
    power = self.names[unit]
    if power < 0:
      if denom == '':
        denom = '\\text{' + unit + '}'
      else:
        denom = denom + '\\cdot \\text{' + unit + '}'
      if power < -1:
        denom = denom + '^' + str(-power)
    elif power > 0:
      if num == '':
        num = '\\text{' + unit + '}'
      else:
        num = num + '\\cdot \\text{' + unit + '}'
      if power > 1:
        num = num + '^{' + str(power) + '}'
  if num == '':
    num = '1'
  if denom != '':
    name = num + '/' + denom
  else:
    name = num
  name = name.replace('\\text{deg}', '\\,^{\\circ}').replace(' pi', ' \\pi ')
  return name


PhysicalUnit._repr_latex_ = _repr_latex_


class PQ:
  pq: PhysicalQuantity | float

  def __init__(self, pq: PQ | PhysicalQuantity | str | float):
    if isinstance(pq, PQ):
      self.pq = pq.pq
    elif isinstance(pq, PhysicalQuantity):
      self.pq = pq
    elif isinstance(pq, str):
      if pq == '1':
        self.pq = PhysicalQuantity(1, 'm/m')
      else:
        try:
          self.pq = PhysicalQuantity(1, pq)
        except UnitError as e:
          raise e
    else:
      self.pq = 1

  def __str__(self) -> str:
    if isinstance(self.pq, PhysicalQuantity):
      return f'[{str(self.pq.unit)}]'
    else:
      return '[1]'

  def __repr__(self) -> str:
    if isinstance(self.pq, PhysicalQuantity):
      return f'PQ(\'{str(self.pq.unit)}\')'
    else:
      return 'PQ(1)'

  def _repr_latex_(self) -> str:
    if isinstance(self.pq, PhysicalQuantity):
      return f'[{self.pq.unit._repr_latex_()}]'
    else:
      return '[1]'

  def __add__(self, other: PQ) -> PQ:
    return PQ(self.pq + other.pq)

  def __mul__(self, other: Any) -> PQ:
    if isinstance(other, PQ):
      return PQ(self.pq * other.pq)
    else:
      return PQ(self.pq * other)

  def __truediv__(self, other: Any) -> PQ:
    if isinstance(other, PQ):
      return PQ(self.pq / other.pq)
    else:
      return PQ(self.pq / other)

  def __pow__(self, other: Any) -> PQ:
    return PQ(self.pq.__pow__(other))


class ExprWithUnit:
  """
  Expr with a unit.
  """
  expr: Expr
  pq: PQ

  def __init__(self, expr: Expr | str, pq: PQ | str | float) -> None:
    if isinstance(expr, str):
      self.expr = Symbol(expr)  # type: ignore
    else:
      self.expr = expr

    self.pq = PQ(pq)

  def __str__(self) -> str:
    return f'{str(nsimplify(self.expr))} {str(self.pq)}'

  @property
  def to_key(self) -> str:
    return str(nsimplify(self.expr))

  def __repr__(self) -> str:
    return f'ExprWithUnit(\'{str(nsimplify(self.expr))}\', {repr(self.pq)})'

  def _repr_latex_(self) -> str:
    """
    Return latex representation for IPython notebook
    """
    return latex(nsimplify(self.expr)) + '~' + self.pq._repr_latex_()  # type: ignore

  def convert_to_base(self) -> ExprWithUnit:
    if isinstance(self.pq.pq, PhysicalQuantity):
      factor = self.pq.pq.base.value
      base_unit = self.pq.pq.base.unit
      return ExprWithUnit(factor * self.expr, PhysicalQuantity(1, str(base_unit)))
    else:
      return self

  def __eq__(self, other: object) -> bool:
    if isinstance(other, ExprWithUnit):
      return str(self) == str(other)
    else:
      return False

  def __add__(self, other: ExprWithUnit) -> ExprWithUnit:
    factor = other.factor_to(self)
    return ExprWithUnit(self.expr + other.expr * factor, self.pq)

  def __sub__(self, other: ExprWithUnit) -> ExprWithUnit:
    factor = other.factor_to(self)
    return ExprWithUnit(self.expr - other.expr * factor, self.pq)

  def __mul__(self, other: Any) -> ExprWithUnit:
    if isinstance(other, ExprWithUnit):
      s = self.convert_to_base()
      o = other.convert_to_base()
      return ExprWithUnit(s.expr * o.expr, s.pq * o.pq)
    else:
      return ExprWithUnit(self.expr * other, self.pq)

  def __rmul__(self, other: Any) -> ExprWithUnit:
    return ExprWithUnit(self.expr * other, self.pq)

  def __truediv__(self, other: Any) -> ExprWithUnit:
    if isinstance(other, ExprWithUnit):
      s = self.convert_to_base()
      o = other.convert_to_base()
      return ExprWithUnit(s.expr / o.expr, s.pq / o.pq)
    else:
      return ExprWithUnit(self.expr / other, self.pq)

  def __pow__(self, other: Any) -> ExprWithUnit:
    return ExprWithUnit(self.expr ** other, self.pq ** other)

  def factor_to(self, other: ExprWithUnit) -> float:
    self.pq + other.pq
    if isinstance(self.pq.pq, PhysicalQuantity):
      return self.pq.pq.unit.conversion_factor_to(other.pq.pq.unit)  # type: ignore
    else:
      return 1
