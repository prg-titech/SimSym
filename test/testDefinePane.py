import unittest

from SimSym.exception import (EmptyException, ObjAlreadyDefinedException,
                              VarAlreadyDefinedException)
from SimSym.gui import (DefinePane, EquationWidget, GlobalVarWidget,
                        ObjGenerateWidget, ObjVarWidget)
from SimSym.model import EquationHolder, Obj, VariableHolder
from SimSym.unit import EqWithUnit, ExprWithUnit


class TestDefinePane(unittest.TestCase):
  def test_all(self) -> None:
    vh = VariableHolder()
    eh = EquationHolder()
    obj_generate_widget = ObjGenerateWidget()
    obj_var_widget = ObjVarWidget(vh)
    global_var_widget = GlobalVarWidget(vh)
    equation_widget = EquationWidget(eh)
    def_pane = DefinePane(obj_generate_widget, obj_var_widget, global_var_widget, equation_widget)
    self.assertTrue(isinstance(def_pane, DefinePane))

    obj_var_widget.add_object(Obj('A', vh))
    with self.assertRaises(VarAlreadyDefinedException):
      obj_var_widget.add_object(Obj('A', vh))

    obj_var_widget.add_object_by_name('B')
    with self.assertRaises(ObjAlreadyDefinedException):
      obj_var_widget.add_object_by_name('B')

    obj_generate_widget.text_input.value = 'C'
    obj_generate_widget.button.click()
    with self.assertRaises(ObjAlreadyDefinedException):
      obj_var_widget.add_object_by_name('C')

    with self.assertRaises(EmptyException):
      obj_var_widget.add_object_by_name('')

    obj_var_widget.children[0].add(ExprWithUnit('a_A', 'm/s^2'))
    with self.assertRaises(VarAlreadyDefinedException):
      obj_var_widget.children[0].add(ExprWithUnit('a_A', 'm/s^2'))

    global_var_widget.add(ExprWithUnit('a', 'm/s/s'))
    with self.assertRaises(VarAlreadyDefinedException):
      global_var_widget.add(ExprWithUnit('a', 'm/s/s'))

    equation_widget.add(EqWithUnit(ExprWithUnit('x', 'm'), ExprWithUnit('y', 'm')))
    with self.assertRaises(ValueError):
      equation_widget.add(EqWithUnit(ExprWithUnit('x', 'm'), ExprWithUnit('y', 'm')))
