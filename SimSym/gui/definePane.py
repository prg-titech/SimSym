from ipywidgets import Layout, Tab, VBox

from ..model import EquationHolder, VariableHolder
from .equationWidget import EquationWidget
from .globalVarWidget import GlobalVarWidget
from .objGenerateWidget import ObjGenerateWidget
from .objVarWidget import ObjVarWidget


class DefinePane(Tab):  # type: ignore
  variable_holder: VariableHolder
  equation_holder: EquationHolder
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
      variable_holder: VariableHolder | None = None,
      equation_holder: EquationHolder | None = None,
  ) -> None:
    self.variable_holder = variable_holder or VariableHolder()
    self.equation_holder = equation_holder or EquationHolder()
    self.obj_generate_widget = obj_generate_widget or ObjGenerateWidget()
    self.obj_var_widget = obj_var_widget or ObjVarWidget(self.variable_holder)
    self.global_var_widget = global_var_widget or GlobalVarWidget(self.variable_holder)
    self.equation_widget = equation_widget or EquationWidget(self.equation_holder)

    self.obj_generate_widget.set_callback(self.obj_var_widget)
    self.global_var_widget.set_callback()
    self.equation_widget.set_callback(self.variable_holder)

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
