"""Generate diff module."""

import json


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


def generate_diff(first_file: str, second_file: str) -> str:
    """
    Return the difference between two flat json files.

    Args:
        first_file: first file path
        second_file: second file path

    Returns:
        str

    """
    first_json = json.load(first_file.open())  # noqa: WPS515
    second_json = json.load(second_file.open())  # noqa: WPS515
    json_items = []
    for key in get_keys(first_json, second_json):
        if first_json.get(key) == second_json.get(key):
            json_items.append('    {0}: {1}'.format(key, first_json.get(key)))
            continue
        if key in first_json:
            json_items.append('  - {0}: {1}'.format(key, first_json.get(key)))
        if key in second_json:
            json_items.append('  + {0}: {1}'.format(key, second_json.get(key)))
    json_items.insert(0, '{')
    json_items.append('}')
    return '\n'.join(json_items)
