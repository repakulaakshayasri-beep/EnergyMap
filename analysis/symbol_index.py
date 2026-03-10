import ast
from pathlib import Path
from typing import Dict


def build_symbol_index(src_root: Path) -> Dict[str, Path]:
    """
    Walk src_root and build a mapping:
        symbol_name -> file_path

    Indexed symbols:
        - Top-level functions
        - Classes
        - Class methods
    """

    symbol_index: Dict[str, Path] = {}

    for py_file in src_root.rglob("*.py"):
        try:
            source = py_file.read_text(encoding="utf-8")
            tree = ast.parse(source)
        except Exception:
            continue  # Skip files that fail parsing

        for node in tree.body:

            # Top-level function
            if isinstance(node, ast.FunctionDef):
                symbol_index[node.name] = py_file

            # Class
            elif isinstance(node, ast.ClassDef):
                symbol_index[node.name] = py_file

                # Class methods
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        symbol_index[item.name] = py_file

    return symbol_index