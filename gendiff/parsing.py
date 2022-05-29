"""Parse module."""

import json
from pathlib import Path

import yaml


def parse_file(path: Path) -> dict:
    """Parse json and yaml files.

    Args:
        path: path to file

    Returns:
        dict

    Raises:
        AttributeError: if file format unsupported
    """
    if path.name.endswith('.json'):
        return json.load(path.open())
    elif path.name.endswith('.yaml') or path.name.endswith('.yml'):
        return yaml.safe_load(path.open())
    raise AttributeError('Unsupported file format')
