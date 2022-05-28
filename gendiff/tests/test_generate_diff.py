"""Test module."""
from pathlib import Path

from gendiff.flat import generate_diff


def test_generate_diff():
    """Test for generate_diff function."""
    first_path = Path(Path.cwd(), 'gendiff/tests/fixtures/file1.json')
    second_path = Path(Path.cwd(), 'gendiff/tests/fixtures/file2.json')
    result_path = Path(Path.cwd(), 'gendiff/tests/fixtures/result.txt')
    expected_result = result_path.read_text()
    assert generate_diff(first_path, second_path) == expected_result
