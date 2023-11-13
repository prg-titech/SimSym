import unittest

from SimSym import EqWithUnit, ExprWithUnit
from SimSym.model import EquationHolder


class TestEquationHolder(unittest.TestCase):
  def test_add(self) -> None:
    eh = EquationHolder()
    x = ExprWithUnit('x', 'm')
    y = ExprWithUnit('y', 'm')
    eq = EqWithUnit(x, y)
    eh.add(eq)
    self.assertEqual(eh.equations[str(eq)], eq)
    with self.assertRaises(ValueError):
      eh.add(eq)
