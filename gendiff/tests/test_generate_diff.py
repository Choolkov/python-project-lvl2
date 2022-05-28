"""Test module."""
from pathlib import Path

from gendiff.flat import generate_diff
from pytest import fixture


@fixture
def tests_directory() -> Path:
    """.

    Returns:
        path object of tests directory.
    """
    return Path(__file__).parent


def test_generate_diff(tests_directory):
    """
    Test for generate_diff function.

    Args:
        tests_directory: fixture
    """
    first_path = Path(tests_directory, 'fixtures/file1.json')
    second_path = Path(tests_directory, 'fixtures/file2.json')
    result_path = Path(tests_directory, 'fixtures/result.txt')
    expected_result = result_path.read_text()
    assert generate_diff(first_path, second_path) == expected_result
