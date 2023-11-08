import unittest

from PhysicalQuantities.unit import UnitError

from SimSym import ExprWithUnit


class TestExprWithUnit(unittest.TestCase):
  def test_eq(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    self.assertEqual(a, a)
    self.assertNotEqual(a, b)
    self.assertNotEqual(a, 100)

  def test_add(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = a + b
    self.assertEqual(str(c), 'a + b [m]')
    self.assertEqual(repr(c), 'ExprWithUnit(a + b, PQ(m))')
    self.assertEqual(c._repr_latex_(), 'a + b~[\\text{m}]')

  def test_unit_key_error(self) -> None:
    with self.assertRaises(UnitError):
      ExprWithUnit('a', 'meters')

  def test_sub(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = a - b
    self.assertEqual(str(c), 'a - b [m]')
    self.assertEqual(repr(c), 'ExprWithUnit(a - b, PQ(m))')
    self.assertEqual(c._repr_latex_(), 'a - b~[\\text{m}]')

  def test_mul(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = a * b
    self.assertEqual(str(c), 'a*b [m^2]')
    self.assertEqual(repr(c), 'ExprWithUnit(a*b, PQ(m^2))')
    self.assertEqual(c._repr_latex_(), 'a b~[\\text{m}^{2}]')

  def test_mul_any(self) -> None:
    a = ExprWithUnit('a', 'm')
    c = a * 2.0
    self.assertEqual(str(c), '2*a [m]')
    self.assertEqual(repr(c), 'ExprWithUnit(2*a, PQ(m))')
    self.assertEqual(c._repr_latex_(), '2 a~[\\text{m}]')

  def test_rmul_any(self) -> None:
    a = ExprWithUnit('a', 'm')
    c = 2 * a
    self.assertEqual(str(c), '2*a [m]')
    self.assertEqual(repr(c), 'ExprWithUnit(2*a, PQ(m))')
    self.assertEqual(c._repr_latex_(), '2 a~[\\text{m}]')

  def test_truediv(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = a / b
    self.assertEqual(str(c), 'a/b [1]')
    self.assertEqual(repr(c), 'ExprWithUnit(a/b, PQ(1))')
    self.assertEqual(c._repr_latex_(), '\\frac{a}{b}~[1]')

  def test_truediv_any(self) -> None:
    a = ExprWithUnit('a', 'm')
    c = a / 2.0
    self.assertEqual(str(c), 'a/2 [m]')
    self.assertEqual(repr(c), 'ExprWithUnit(a/2, PQ(m))')
    self.assertEqual(c._repr_latex_(), '\\frac{a}{2}~[\\text{m}]')

  def test_pow(self) -> None:
    a = ExprWithUnit('a', 'm')
    c = a ** 2
    self.assertEqual(str(c), 'a**2 [m^2]')
    self.assertEqual(repr(c), 'ExprWithUnit(a**2, PQ(m^2))')
    self.assertEqual(c._repr_latex_(), 'a^{2}~[\\text{m}^{2}]')

  def test_factor_to(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'cm')
    self.assertEqual(a.factor_to(b), 100.0)
    self.assertEqual(b.factor_to(a), 0.01)
    self.assertEqual((a / b + a / b)._repr_latex_(), '\\frac{200 a}{b}~[1]')

  def test_convert_to_base(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'mm')
    self.assertEqual(a.convert_to_base(), a)
    self.assertEqual(b.convert_to_base(), ExprWithUnit('b', 'm') / 1000)
    self.assertEqual((a / b)._repr_latex_(), '\\frac{1000 a}{b}~[1]')
    self.assertEqual((a / b * b)._repr_latex_(), 'a~[\\text{m}]')
