from ipywidgets import Layout, Tab, VBox

from ..model import EquationHolder, VariableHolder
from .equationWidget import EquationWidget
from .globalVarWidget import GlobalVarWidget
from .objGenerateWidget import ObjGenerateWidget
from .objVarWidget import ObjVarWidget


class DefinePane(Tab):  # type: ignore
  variableHolder: VariableHolder
  equationHolder: EquationHolder
  obj_generate_widget: ObjGenerateWidget
  obj_var_widget: ObjVarWidget
  global_var_widget: GlobalVarWidget
  equation_widget: EquationWidget

  def __init__(
      self,
      obj_generate_widget: ObjGenerateWidget | None = None,
      obj_var_widget: ObjVarWidget | None = None,
      global_var_widget: GlobalVarWidget | None = None,
      equation_widget: EquationWidget | None = None,
      variableHolder: VariableHolder | None = None,
      equationHolder: EquationHolder | None = None,
  ) -> None:
    self.variableHolder = variableHolder or VariableHolder()
    self.equationHolder = equationHolder or EquationHolder()
    self.obj_generate_widget = obj_generate_widget or ObjGenerateWidget()
    self.obj_var_widget = obj_var_widget or ObjVarWidget(self.variableHolder)
    self.global_var_widget = global_var_widget or GlobalVarWidget(self.variableHolder)
    self.equation_widget = equation_widget or EquationWidget(self.equationHolder)

    super().__init__(
        children=[VBox([
            self.obj_generate_widget,
            self.obj_var_widget,
            self.global_var_widget,
            self.equation_widget
        ])],
        layout=Layout(width='45%')
    )

    self.set_title(0, '物理系定義ペイン')
