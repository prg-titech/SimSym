import unittest

from SimSym import Main
from SimSym.utility.parseWithUnit import parse_with_unit


class TestObservePane(unittest.TestCase):
  def test_all(self) -> None:
    main = Main()
    define_pane = main.define_pane
    observe_pane = main.observe_pane

    self.assertEqual(define_pane.variable_holder, observe_pane.variable_holder)
    self.assertEqual(define_pane.equation_holder, observe_pane.equation_holder)

    # AxisSetWidget のテスト
    axisSetWidget = observe_pane.axes_set_widget
    visualizeWidget = observe_pane.visualize_widget
    variable_holder = define_pane.variable_holder

    axisSetWidget.x_expr_input.text_input.value = 't'
    axisSetWidget.x_expr_input.button.click()
    self.assertEqual(visualizeWidget.x_expr, parse_with_unit('t', variable_holder))

    axisSetWidget.y_expr_input.text_input.value = 'g'
    axisSetWidget.y_expr_input.button.click()
    self.assertEqual(visualizeWidget.y_expr, parse_with_unit('g', variable_holder))

    # 空の状態で押すと何も起きない
    axisSetWidget.x_expr_input.button.click()

    # 存在しない変数を設定するとエラー
    axisSetWidget.y_expr_input.text_input.value = 'f'
    axisSetWidget.y_expr_input.button.click()
