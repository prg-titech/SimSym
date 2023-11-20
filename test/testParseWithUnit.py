import unittest

from SimSym.model.variableHolder import VariableHolder
from SimSym.unit.exprWithUnit import ExprWithUnit
from SimSym.utility import parse_with_unit


class TestParseWithUnit(unittest.TestCase):
  def test(self) -> None:
    vh = VariableHolder()
    vh.add(ExprWithUnit('x', 'm'))
    vh.add(ExprWithUnit('y', 'm'))

    expr1 = parse_with_unit('x+y', vh)
    self.assertEqual(str(expr1), 'x + y [m]')

    expr2 = parse_with_unit('x*y', vh)
    self.assertEqual(str(expr2), 'x*y [m^2]')
    self.assertEqual(expr2._repr_latex_(), 'x y~[\\text{m}^{2}]')
