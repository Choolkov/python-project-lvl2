"""Paths to fixtures."""
from pathlib import Path

TESTS = Path(__file__).parent

FIXTURES = Path(TESTS, 'fixtures')

JSON_FIRST_FILE = Path(FIXTURES, 'file1.json')
JSON_SECOND_FILE = Path(FIXTURES, 'file2.json')
JSON_THIRD_FILE = Path(FIXTURES, 'file3.json')
JSON_FOURTH_FILE = Path(FIXTURES, 'file4.json')

YAML_FIRST_FILE = Path(FIXTURES, 'file1.yaml')
YAML_SECOND_FILE = Path(FIXTURES, 'file2.yaml')
YAML_THIRD_FILE = Path(FIXTURES, 'file3.yaml')
YAML_FOURTH_FILE = Path(FIXTURES, 'file4.yaml')

DIFFS = Path(FIXTURES, 'diffs')
FLAT_DIFF_FILE = Path(DIFFS, 'flat_diff.txt')
RECURSIVE_DIFF_FILE = Path(DIFFS, 'recursive_diff.txt')
