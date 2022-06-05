"""Paths to fixtures."""
from pathlib import Path

TESTS = Path(__file__).parent

FIXTURES = Path(TESTS, 'fixtures')

JSON_FIRST_FILE = Path(FIXTURES, 'file1.json')
JSON_SECOND_FILE = Path(FIXTURES, 'file2.json')

YAML_FIRST_FILE = Path(FIXTURES, 'file1.yaml')
YAML_SECOND_FILE = Path(FIXTURES, 'file2.yaml')

DIFFS = Path(FIXTURES, 'diffs')

DIFF_STYLISH_FILE = Path(DIFFS, 'stylish_diff.txt')
DIFF_PLAIN_FILE = Path(DIFFS, 'plain_diff.txt')
DIFF_JSON_FILE = Path(DIFFS, 'json_diff.txt')
