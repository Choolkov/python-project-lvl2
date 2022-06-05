"""Generate diff module."""

from pathlib import Path

from gendiff.parsing import parse_file
from gendiff.tree import build_tree
from gendiff.views.json import get_json
from gendiff.views.plain import get_plain
from gendiff.views.stylish import get_stylish


def generate_diff(
    first_file: Path,
    second_file: Path,
    format_name='stylish',
) -> str:
    """
    Return the difference between two flat json or yaml files.

    Args:
        first_file: first file path
        second_file: second file path
        format_name: diff output format

    Returns:
        str

    """
    first_dict = parse_file(first_file)
    second_dict = parse_file(second_file)
    tree = build_tree(first_dict, second_dict)
    views = {'stylish': get_stylish, 'plain': get_plain, 'json': get_json}
    return views[format_name](tree)
