import unittest

from PhysicalQuantities.unit import UnitError

from SimSym.unit.exprWithUnit import PQ


class TestPQ(unittest.TestCase):
  def test_repr_latex(self) -> None:
    a = PQ('m') / PQ('s') / PQ('kg') * PQ('rad')
    self.assertEqual(a._repr_latex_(), '[\\text{m}\\cdot \\text{rad}/\\text{s}\\cdot \\text{kg}]')
    b = PQ(1) / PQ('m')
    self.assertEqual(b._repr_latex_(), '[1/\\text{m}]')

  def test_eq_keyerror(self) -> None:
    with self.assertRaises(UnitError):
      PQ('meters')

  def test_mul_to_any(self) -> None:
    a = PQ('m')
    c = a * 2.0
    self.assertEqual(str(c), '[m]')
    self.assertEqual(repr(c), 'PQ(\'m\')')
    self.assertEqual(c._repr_latex_(), '[\\text{m}]')

  def test_truediv_to_any(self) -> None:
    a = PQ('m')
    c = a / 2.0
    self.assertEqual(str(c), '[m]')
    self.assertEqual(repr(c), 'PQ(\'m\')')
    self.assertEqual(c._repr_latex_(), '[\\text{m}]')
