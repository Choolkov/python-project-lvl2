"""Paths to fixtures."""
from pathlib import Path

TESTS = Path(__file__).parent

FIXTURES = Path(TESTS, 'fixtures')
JSON_FIRST_FILE = Path(FIXTURES, 'file1.json')
JSON_SECOND_FILE = Path(FIXTURES, 'file2.json')

DIFFS = Path(FIXTURES, 'diffs')
JSON_DIFF_FILE = Path(DIFFS, 'json_diff.txt')
