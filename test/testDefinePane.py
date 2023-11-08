import unittest

from SimSym.gui import (DefinePane, EquationWidget, GlobalVarWidget,
                        ObjGenerateWidget, ObjVarWidget)
from SimSym.model import Obj
from SimSym.unit import EqWithUnit, ExprWithUnit


class TestDefinePane(unittest.TestCase):
  def test_all(self) -> None:
    obj_generate_widget = ObjGenerateWidget()
    obj_var_widget = ObjVarWidget()
    global_var_widget = GlobalVarWidget()
    equation_widget = EquationWidget()
    def_pane = DefinePane(obj_generate_widget, obj_var_widget, global_var_widget, equation_widget)
    self.assertTrue(isinstance(def_pane, DefinePane))

    obj_var_widget.add_object(Obj('A'))
    with self.assertRaises(ValueError):
      obj_var_widget.add_object(Obj('A'))

    obj_var_widget.children[0].add(ExprWithUnit('a_A', 'm/s^2'))
    with self.assertRaises(ValueError):
      obj_var_widget.children[0].add(ExprWithUnit('a_A', 'm/s^2'))

    global_var_widget.add(ExprWithUnit('a', 'm/s/s'))
    with self.assertRaises(ValueError):
      global_var_widget.add(ExprWithUnit('a', 'm/s/s'))

    equation_widget.add(EqWithUnit(ExprWithUnit('x', 'm'), ExprWithUnit('y', 'm')))
    with self.assertRaises(ValueError):
      equation_widget.add(EqWithUnit(ExprWithUnit('x', 'm'), ExprWithUnit('y', 'm')))
