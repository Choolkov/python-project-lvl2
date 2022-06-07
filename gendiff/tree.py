"""Generate diff module for recursive structures."""
from collections import namedtuple

Node = namedtuple('Node', ['type', 'value'])


def build_tree(dict1: dict, dict2: dict) -> dict:  # NOQA WPS232
    """
    Return the diff of two dictionaries.

    Args:
        dict1: first dictionary
        dict2: second dictionary

    Returns:
        dict

    """
    diff = {}
    keys = sorted(dict1.keys() | dict2.keys())
    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict1:
            diff[key] = Node('added', value2)  # NOQA WPS204
        elif key not in dict2:
            diff[key] = Node('removed', value1)
        elif value1 == value2:
            diff[key] = Node('unchanged', value1)
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = Node('nested', build_tree(value1, value2))
        else:
            diff[key] = Node('changed', (value1, value2))
    return diff
