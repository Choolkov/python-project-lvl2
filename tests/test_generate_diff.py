"""Tests for generate_diff function."""
import pytest
from gendiff.gendiff import generate_diff
from tests.fixtures_paths import (
    DIFF_JSON_FILE,
    DIFF_PLAIN_FILE,
    DIFF_STYLISH_FILE,
    JSON_FIRST_FILE,
    JSON_SECOND_FILE,
    YAML_FIRST_FILE,
    YAML_SECOND_FILE,
)


@pytest.mark.parametrize(
    'first_file,second_file,diff,format_name',
    [
        (JSON_FIRST_FILE, JSON_SECOND_FILE, DIFF_STYLISH_FILE, 'stylish'),
        (JSON_FIRST_FILE, JSON_SECOND_FILE, DIFF_PLAIN_FILE, 'plain'),
        (JSON_FIRST_FILE, JSON_SECOND_FILE, DIFF_JSON_FILE, 'json'),
        (YAML_FIRST_FILE, YAML_SECOND_FILE, DIFF_STYLISH_FILE, 'stylish'),
        (YAML_FIRST_FILE, YAML_SECOND_FILE, DIFF_PLAIN_FILE, 'plain'),
        (YAML_FIRST_FILE, YAML_SECOND_FILE, DIFF_JSON_FILE, 'json'),
    ],
)
def test_generate_diff(first_file, second_file, diff, format_name):
    """Tests the generate_diff function.

    Args:
        first_file: first file path
        second_file: second file path
        diff: expected diff path
        format_name: format name
    """
    with open(diff) as file:  # NOQA: WPS110
        expected_diff = file.read()
    diff = generate_diff(first_file, second_file, format_name)
    assert diff == expected_diff
