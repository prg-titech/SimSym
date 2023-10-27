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
