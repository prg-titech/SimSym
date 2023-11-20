import unittest

from PhysicalQuantities.unit import UnitError

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

    vh.add(ExprWithUnit('t', 's'))
    with self.assertRaises(UnitError):
      parse_with_unit('x+t', vh)

    expr2 = parse_with_unit('x*y', vh)
    self.assertEqual(str(expr2), 'x*y [m^2]')
    self.assertEqual(expr2._repr_latex_(), 'x y~[\\text{m}^{2}]')
