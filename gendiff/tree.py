"""Generate diff module for recursive structures."""
from collections import namedtuple

Node = namedtuple('Node', ['name', 'status', 'values'])


def make_node(name, status, values):
    return Node(name, status, values)

def build_tree(dict1: dict, dict2: dict) -> dict:
    """
    Return the diff of two dictionaries.

    Args:
        dict1: first dictionary
        dict2: second dictionary

    Returns:
        dict

    """
    diff = []
    keys = sorted(dict1.keys() | dict2.keys())
    for key in keys:
        if key not in dict1:
            diff.append(make_node(key, 'added', dict2[key]))
        elif key not in dict2:
            diff.append(make_node(key, 'removed', dict1[key]))
        elif dict1[key] == dict2[key]:
            diff.append(make_node(key, 'unchanged', dict1[key]))
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff.append(
                Node(key, 'nested', build_tree(dict1[key], dict2[key])),
            )
        else:
            diff.append(Node(key, 'changed', (dict1[key], dict2[key])))
    return diff
