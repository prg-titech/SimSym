from ipywidgets import Layout, Tab, VBox, Widget


class DefinePane(Tab):  # type: ignore
  def __init__(
      self,
      obj_generate_widget: Widget,
      obj_var_widget: Widget,
      global_var_widget: Widget,
      equation_widget: Widget,
  ) -> None:
    super().__init__(
        children=[VBox([
            obj_generate_widget,
            obj_var_widget,
            global_var_widget,
            equation_widget
        ])],
        layout=Layout(width='45%')
    )
    self.obj_generate_widget = obj_generate_widget
    self.obj_var_widget = obj_var_widget
    self.global_var_widget = global_var_widget
    self.equation_widget = equation_widget
    self.set_title(0, '物理系定義ペイン')
