"""Test module."""
from gendiff.flat import generate_diff
from gendiff.parsing import parse_file
from gendiff.tree import build_tree
from gendiff.views.stylish import get_stylish
from tests.fixtures_paths import (
    FLAT_DIFF_FILE,
    JSON_FIRST_FILE,
    JSON_FOURTH_FILE,
    JSON_SECOND_FILE,
    JSON_THIRD_FILE,
    RECURSIVE_DIFF_FILE,
    YAML_FIRST_FILE,
    YAML_FOURTH_FILE,
    YAML_SECOND_FILE,
    YAML_THIRD_FILE,
)


def test_generate_diff():
    """Test for generate_diff function."""
    expected_diff = FLAT_DIFF_FILE.read_text()
    assert generate_diff(JSON_FIRST_FILE, JSON_SECOND_FILE) == expected_diff
    assert generate_diff(YAML_FIRST_FILE, YAML_SECOND_FILE) == expected_diff

def test_generate_diff_recursive():
    """Test for generate_diff function recursive."""
    expected_diff = RECURSIVE_DIFF_FILE.read_text()
    fixture1 = parse_file(JSON_THIRD_FILE)
    fixture2 = parse_file(JSON_FOURTH_FILE)
    fixture3 = parse_file(YAML_THIRD_FILE)
    fixture4 = parse_file(YAML_FOURTH_FILE)
    assert get_stylish(build_tree(fixture1, fixture2)) == expected_diff
    assert get_stylish(build_tree(fixture3, fixture4)) == expected_diff
