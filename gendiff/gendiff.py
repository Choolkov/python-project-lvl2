"""Generate diff module."""

from pathlib import Path

from gendiff.io import get_extension, load_content
from gendiff.parsing import parse_content
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
    first_file_content = parse_content(
        load_content(first_file), get_extension(first_file),
    )
    second_file_content = parse_content(
        load_content(second_file), get_extension(second_file),
    )
    views = {'stylish': get_stylish, 'plain': get_plain, 'json': get_json}
    return views[format_name](
        build_tree(first_file_content, second_file_content),
    )
