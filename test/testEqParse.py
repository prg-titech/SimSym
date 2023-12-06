import unittest
from SimSym.exception.exception import IllegalEquationException

from SimSym.gui import DefinePane
from SimSym.utility.alert import alert_exception


class TestEqParse(unittest.TestCase):
  def test_all(self) -> None:
    def_pane = DefinePane()

    # 物体生成
    def_pane.obj_generate_widget.text_input.value = 'A'
    def_pane.obj_generate_widget.button.click()
    self.assertTrue('x_A' in def_pane.variable_holder.variables.keys())

    # 方程式の追加
    equation_add_widget = def_pane.equation_widget.add_widget
    equation_add_widget.text_input.value = 'x_A = y_A'
    equation_add_widget.button.click()
    self.assertEqual(equation_add_widget.text_input.value, '')

    # 例外
    equation_add_widget.text_input.value = 'x_A'
    equation_add_widget.button.click()

    equation_add_widget.text_input.value = 'x_A = y_p'
    equation_add_widget.button.click()
