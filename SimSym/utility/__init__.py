from .alert import AlertOutput, alert, alert_exception
from .nsimplify import nsimplify

__all__ = [
    'nsimplify',
    'alert',
    'alert_exception',
]

from IPython.display import display

display(AlertOutput().out)  # type: ignore
