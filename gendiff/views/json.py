"""JSON output format module."""
import json


def get_json(tree: list) -> str:
    return json.dumps(tree, indent=4)
