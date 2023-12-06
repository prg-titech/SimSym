from ipywidgets import HBox

from ..model import EquationHolder, VariableHolder
from .definePane import DefinePane
from .observePane import ObservePane


class Main(HBox):  # type: ignore
  define_pane: DefinePane
  observe_pane: ObservePane

  def __init__(
      self,
      variable_holder: VariableHolder | None = None,
      equation_holder: EquationHolder | None = None,
      define_pane: DefinePane | None = None,
      observe_pane: ObservePane | None = None,
  ) -> None:
    self.variable_holder = variable_holder or VariableHolder()
    self.equation_holder = equation_holder or EquationHolder()
    self.define_pane = define_pane or DefinePane(
        variable_holder=self.variable_holder,
        equation_holder=self.equation_holder,
    )
    self.observe_pane = observe_pane or ObservePane(
        variable_holder=self.variable_holder,
        equation_holder=self.equation_holder,
    )
    super().__init__(children=[self.define_pane, self.observe_pane or ObservePane()])
