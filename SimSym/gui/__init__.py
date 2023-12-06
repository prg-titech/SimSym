from IPython.display import display
from ipywidgets import HTML

from .definePane import DefinePane
from .equationWidget import EquationWidget
from .globalVarWidget import GlobalVarWidget
from .main import Main
from .objGenerateWidget import ObjGenerateWidget
from .objVarWidget import ObjVarWidget
from .observePane import ObservePane

# GUI にスタイルを適用する
display(HTML('''
<style>
.flexgrid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
}
div.widget-label-small > .widget-label {
    width: 1px;
}
div.widget-label-example > .widget-label {
    width: 60px;
}
table {float:left}
</style>
'''))  # type: ignore


__all__ = [
    'Main',
    'DefinePane',
    'ObjGenerateWidget',
    'ObjVarWidget',
    'GlobalVarWidget',
    'EquationWidget',
    'ObservePane'
]
