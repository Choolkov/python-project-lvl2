"""Parse module."""

import json
from pathlib import Path
from typing import Union

import yaml


def parse_file(path: Union[Path, str]) -> dict:
    """Parse json and yaml files.

    Args:
        path: path to file

    Returns:
        dict

    Raises:
        AttributeError: if file format unsupported
    """
    if isinstance(path, str):
        path = Path(path)
    if path.name.endswith('.json'):
        return json.load(path.open())
    elif path.name.endswith('.yaml') or path.name.endswith('.yml'):
        return yaml.safe_load(path.open())
    raise AttributeError('Unsupported file format')
