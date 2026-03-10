import ast
from typing import Set


def extract_called_symbols(func_node: ast.FunctionDef) -> Set[str]:
    """
    Walk the AST of a function and collect all symbol names
    that appear in function calls or attribute access.

    Returns:
        set of symbol names (strings)
    """

    symbols: Set[str] = set()

    for node in ast.walk(func_node):

        # Direct function calls: foo()
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                symbols.add(node.func.id)

            elif isinstance(node.func, ast.Attribute):
                symbols.add(node.func.attr)

        # Attribute access: black.main
        elif isinstance(node, ast.Attribute):
            symbols.add(node.attr)

        # Name usage
        elif isinstance(node, ast.Name):
            symbols.add(node.id)

    return symbols