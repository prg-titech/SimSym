import unittest

from SimSym import Main


class TestObservePane(unittest.TestCase):
  def test_all(self) -> None:
    main = Main()
    define_pane = main.define_pane
    observe_pane = main.observe_pane

    self.assertEqual(define_pane.variable_holder, observe_pane.variable_holder)
    self.assertEqual(define_pane.equation_holder, observe_pane.equation_holder)
