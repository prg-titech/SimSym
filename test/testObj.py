import unittest

from SimSym.model import Obj, VariableHolder


class TestObj(unittest.TestCase):
  def test_init(self) -> None:
    vh = VariableHolder()
    a = Obj('A', vh)
    self.assertEqual(a.name, 'A')
    self.assertEqual(repr(a), 'Obj(A)')

  def test_eq(self) -> None:
    vh = VariableHolder()
    a = Obj('A', vh)
    b = Obj('B', vh)
    self.assertEqual(a, a)
    self.assertNotEqual(a, b)
    self.assertNotEqual(a, 100)
