import unittest

from SimSym import ExprWithUnit
from SimSym.model import VariableHolder


class TestVariableHolder(unittest.TestCase):
  def test_add(self) -> None:
    vh = VariableHolder()
    x = ExprWithUnit('x', 'm')
    vh.add(x)
    self.assertEqual(vh.variables[x.to_key], x)
    with self.assertRaises(ValueError):
      vh.add(x)

  def test_get(self) -> None:
    vh = VariableHolder()
    x = ExprWithUnit('x', 'm')
    vh.add(x)
    self.assertEqual(vh.get('x'), x)
    with self.assertRaises(ValueError):
      vh.get('y')