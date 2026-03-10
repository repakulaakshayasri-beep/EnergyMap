import ast
from pathlib import Path
from typing import Dict


def extract_test_methods(test_file: Path) -> Dict[str, ast.FunctionDef]:
    """
    Parse test_file and extract methods inside class BlackTestCase.

    Returns:
        dict[test_method_name] = ast.FunctionDef
    """

    source = test_file.read_text(encoding="utf-8")
    tree = ast.parse(source)

    methods: Dict[str, ast.FunctionDef] = {}

    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "BlackTestCase":

            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    methods[item.name] = item

    return methods