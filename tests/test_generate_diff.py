"""Tests for generate_diff function."""

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

fixtures = {
    'stylish': DIFF_STYLISH_FILE.read_text(),
    'plain': DIFF_PLAIN_FILE.read_text(),
    'json': DIFF_JSON_FILE.read_text(),
}


def test_generate_diff():
    """Test for generate_diff function."""
    for format_name, expected_diff in fixtures.items():
        assert (
            generate_diff(
                JSON_FIRST_FILE, JSON_SECOND_FILE, format_name=format_name,
            )
            == expected_diff
        )

        assert (
            generate_diff(
                YAML_FIRST_FILE, YAML_SECOND_FILE, format_name=format_name,
            )
            == expected_diff
        )
