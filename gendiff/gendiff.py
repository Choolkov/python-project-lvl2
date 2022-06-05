"""Generate diff module."""

from pathlib import Path

from gendiff.parsing import parse_file
from gendiff.tree import build_tree
from gendiff.views.stylish import get_stylish


def generate_diff(first_file: Path, second_file: Path, view='stylish') -> str:
    """
    Return the difference between two flat json or yaml files.

    Args:
        first_file: first file path
        second_file: second file path

    Returns:
        str

    """
    first_dict = parse_file(first_file)
    second_dict = parse_file(second_file)
    tree = build_tree(first_dict, second_dict)
    views = {'stylish': get_stylish}
    return views[view](tree)
