"""Test module."""
from gendiff.flat import generate_diff
from tests.fixtures_paths import (
    JSON_DIFF_FILE,
    JSON_FIRST_FILE,
    JSON_SECOND_FILE,
    YAML_FIRST_FILE,
    YAML_SECOND_FILE,
)


def test_generate_diff():
    """Test for generate_diff function."""
    expected_diff = JSON_DIFF_FILE.read_text()
    assert generate_diff(JSON_FIRST_FILE, JSON_SECOND_FILE) == expected_diff
    assert generate_diff(YAML_FIRST_FILE, YAML_SECOND_FILE) == expected_diff
