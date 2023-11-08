import unittest

from SimSym.model.obj import Obj


class TestObj(unittest.TestCase):
  def test_init(self) -> None:
    a = Obj('A')
    self.assertEqual(a.name, 'A')
    self.assertEqual(repr(a), 'Obj(A)')

  def test_eq(self) -> None:
    a = Obj('A')
    b = Obj('B')
    self.assertEqual(a, a)
    self.assertNotEqual(a, b)
    self.assertNotEqual(a, 100)
