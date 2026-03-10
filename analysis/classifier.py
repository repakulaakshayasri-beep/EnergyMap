from pathlib import Path
from typing import Dict, Set
import ast

from .call_extractor import extract_called_symbols


class TestClassifier:
    """
    Classifies test methods to source files using
    a symbol index.
    """

    def __init__(self, symbol_index: Dict[str, Path]):
        self.symbol_index = symbol_index

    def classify(
        self,
        test_methods: Dict[str, ast.FunctionDef],
        repo_root: Path,
    ) -> Dict[str, Set[Path]]:
        """
        Returns:
            dict[test_method_name] = set[src_file_paths]
        """

        mapping: Dict[str, Set[Path]] = {}

        for test_name, func_node in test_methods.items():
            called_symbols = extract_called_symbols(func_node)

            src_files: Set[Path] = set()

            for symbol in called_symbols:
                if symbol in self.symbol_index:
                    relative_path = self.symbol_index[symbol].relative_to(repo_root)
                    src_files.add(relative_path)

            mapping[test_name] = src_files

        return mapping