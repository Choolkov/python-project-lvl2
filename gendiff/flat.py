"""Generate diff module."""

from pathlib import Path

from gendiff.parsing import parse_file


def get_keys(dictionary1: dict, dictionary2: dict) -> list:
    """
    Return a sorted list of the keys of both dictionaries.

    Args:
        dictionary1: first dictionary
        dictionary2: second dictionary

    Returns:
        list
    """
    keys1 = set(dictionary1.keys())
    keys2 = set(dictionary2.keys())
    return sorted(keys1 | keys2)


def generate_diff(first_file: Path, second_file: Path) -> str:
    """
    Return the difference between two flat json or yaml files.

    Args:
        first_file: first file path
        second_file: second file path

    Returns:
        str

    """
    first_dict = parse_file(first_file)
    second_dict = parse_file(second_file)
    pairs = []
    for key in get_keys(first_dict, second_dict):
        if first_dict.get(key) == second_dict.get(key):
            pairs.append('    {0}: {1}'.format(key, first_dict.get(key)))
            continue
        if key in first_dict:
            pairs.append('  - {0}: {1}'.format(key, first_dict.get(key)))
        if key in second_dict:
            pairs.append('  + {0}: {1}'.format(key, second_dict.get(key)))
    pairs.insert(0, '{')
    pairs.append('}')
    return '\n'.join(pairs)
