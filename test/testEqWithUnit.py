import unittest

from PhysicalQuantities.unit import UnitError

from SimSym import EqWithUnit, ExprWithUnit


class TestEqWithUnit(unittest.TestCase):
  def test_definition(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    eq = EqWithUnit(a, b)
    self.assertEqual(str(eq), 'a=b[m]')
    self.assertEqual(
        repr(eq),
        'EqWithUnit(ExprWithUnit(\'a\', PQ(\'m\')), ExprWithUnit(\'b\', PQ(\'m\')))')
    self.assertEqual(eq._repr_latex_(), 'a=b~[\\text{m}]')

  def test_definition2(self) -> None:
    a = ExprWithUnit('a', 'm^2')
    b = ExprWithUnit('b', 'm')
    with self.assertRaises(UnitError):
      EqWithUnit(a, b)
    self.assertEqual(
        repr(EqWithUnit(a, b * b)),
        'EqWithUnit(ExprWithUnit(\'a\', PQ(\'m^2\')), ExprWithUnit(\'b**2\', PQ(\'m^2\')))'
    )

  def test_eq(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = ExprWithUnit('c', 'm')
    eq1 = EqWithUnit(a, b)
    eq2 = EqWithUnit(a, b)
    eq3 = EqWithUnit(a, c)
    self.assertEqual(eq1, eq2)
    self.assertNotEqual(eq1, eq3)
    self.assertNotEqual(eq1, 'a=b[m]')
