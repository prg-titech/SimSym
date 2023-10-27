import unittest

from SimSym import ExprWithUnit


class TestExprWithUnit(unittest.TestCase):
  def test_add(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = a + b
    self.assertEqual(str(c), 'a + b m')
    self.assertEqual(repr(c), 'a + b m')
    self.assertEqual(c._repr_latex_(), '$a + b~\\mathrm{[\\text{m}]}$')

  def test_unit_key_error(self) -> None:
    with self.assertRaises(KeyError):
      ExprWithUnit('a', 'meters')

  def test_sub(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = a - b
    self.assertEqual(str(c), 'a - b m')
    self.assertEqual(repr(c), 'a - b m')
    self.assertEqual(c._repr_latex_(), '$a - b~\\mathrm{[\\text{m}]}$')

  def test_mul(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = a * b
    self.assertEqual(str(c), 'a*b m^2')
    self.assertEqual(repr(c), 'a*b m^2')
    self.assertEqual(c._repr_latex_(), '$a b~\\mathrm{[\\text{m}^{2}]}$')

  def test_mul_any(self) -> None:
    a = ExprWithUnit('a', 'm')
    c = a * 2.0
    self.assertEqual(str(c), '2*a m')
    self.assertEqual(repr(c), '2*a m')
    self.assertEqual(c._repr_latex_(), '$2 a~\\mathrm{[\\text{m}]}$')

  def test_rmul_any(self) -> None:
    a = ExprWithUnit('a', 'm')
    c = 2 * a
    self.assertEqual(str(c), '2*a m')
    self.assertEqual(repr(c), '2*a m')
    self.assertEqual(c._repr_latex_(), '$2 a~\\mathrm{[\\text{m}]}$')

  def test_truediv(self) -> None:
    a = ExprWithUnit('a', 'm')
    b = ExprWithUnit('b', 'm')
    c = a / b
    self.assertEqual(str(c), 'a/b [1]')
    self.assertEqual(repr(c), 'a/b [1]')
    self.assertEqual(c._repr_latex_(), '$\\frac{a}{b}~\\mathrm{[1]}$')

  def test_pow(self) -> None:
    a = ExprWithUnit('a', 'm')
    c = a ** 2
    self.assertEqual(str(c), 'a**2 m^2')
    self.assertEqual(repr(c), 'a**2 m^2')
    self.assertEqual(c._repr_latex_(), '$a^{2}~\\mathrm{[\\text{m}^{2}]}$')
