"""JSON output format module."""
import json


def get_json(tree: dict) -> str:
    """
    Return a json representation of the diff tree.

    Args:
        tree: diff tree

    Returns:
        str
    """
    return json.dumps(tree, indent=4)
