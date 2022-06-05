"""Test module."""
from gendiff.gendiff import generate_diff
from tests.fixtures_paths import (
    FLAT_DIFF_FILE,
    JSON_DIFF_FILE,
    JSON_FIRST_FILE,
    JSON_FOURTH_FILE,
    JSON_SECOND_FILE,
    JSON_THIRD_FILE,
    NESTED_DIFF_FILE,
    PLAIN_DIFF_FILE,
    YAML_FIRST_FILE,
    YAML_FOURTH_FILE,
    YAML_SECOND_FILE,
    YAML_THIRD_FILE,
)


def test_generate_diff():
    """Test for generate_diff function with flat structure."""
    expected_diff = FLAT_DIFF_FILE.read_text()
    assert generate_diff(JSON_FIRST_FILE, JSON_SECOND_FILE) == expected_diff
    assert generate_diff(YAML_FIRST_FILE, YAML_SECOND_FILE) == expected_diff


def test_generate_diff_nested():
    """Test for generate_diff function with nested structure."""
    expected_diff = NESTED_DIFF_FILE.read_text()
    assert generate_diff(JSON_THIRD_FILE, JSON_FOURTH_FILE) == expected_diff
    assert generate_diff(YAML_THIRD_FILE, YAML_FOURTH_FILE) == expected_diff

def test_generate_diff_plain():
    """Test for generate_diff function with plain output format."""
    expected_diff = PLAIN_DIFF_FILE.read_text()
    assert generate_diff(JSON_THIRD_FILE, JSON_FOURTH_FILE, format_name='plain') == expected_diff
    assert generate_diff(YAML_THIRD_FILE, YAML_FOURTH_FILE, format_name='plain') == expected_diff

def test_generate_diff_json():
    """Test for generate_diff function with json output format."""
    expected_diff = JSON_DIFF_FILE.read_text()
    assert generate_diff(JSON_THIRD_FILE, JSON_FOURTH_FILE, format_name='json') == expected_diff
    assert generate_diff(YAML_THIRD_FILE, YAML_FOURTH_FILE, format_name='json') == expected_diff
