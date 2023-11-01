from ipywidgets import Layout, Tab, VBox, Widget


class DefinePane(Tab):  # type: ignore
  def __init__(
      self,
      object_generate_widget: Widget,
      object_var_widget: Widget,
      global_var_widget: Widget,
      equation_widget: Widget,
  ) -> None:
    super().__init__(
        children=[VBox([
            object_generate_widget,
            object_var_widget,
            global_var_widget,
            equation_widget
        ])],
        layout=Layout(width='45%')
    )
    self.object_generate_widget = object_generate_widget
    self.object_var_widget = object_var_widget
    self.global_var_widget = global_var_widget
    self.equation_widget = equation_widget
    self.set_title(0, '物理系定義ペイン')
