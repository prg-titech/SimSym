from typing import cast

from sympy import Symbol
from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication,
                                        parse_expr, split_symbols,
                                        standard_transformations)

from ..model.variableHolder import VariableHolder
from ..unit.exprWithUnit import PQ, ExprWithUnit

PQ


def parse_with_unit(s: str, vh: VariableHolder) -> ExprWithUnit:
  parsed = parse_expr(s, {}, transformations=standard_transformations +
                      (convert_xor, split_symbols, implicit_multiplication))
  free_symbols = parsed.free_symbols
  replaces: list[tuple[str, ExprWithUnit]] = []
  for symbol in free_symbols:
    PLACEHOLDER = f'__PLACEHOLDER__{str(symbol)}__'
    symbol_with_unit = vh.get(str(symbol))
    parsed = parsed.subs(symbol, Symbol(PLACEHOLDER))  # type: ignore
    replaces.append((PLACEHOLDER, symbol_with_unit))
  expr_str = str(parsed)
  for symbol, symbol_with_unit in replaces:
    expr_str = expr_str.replace(symbol, repr(symbol_with_unit))
  return cast(ExprWithUnit, eval(expr_str))
