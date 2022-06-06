"""Parse module."""

import json

import yaml


def parse_content(string_data: str, extension: str) -> dict:
    """Parse json and yaml data.

    Args:
        string_data: data in string format
        extension: data extension

    Returns:
        dict

    Raises:
        RuntimeError: if extension unsupported
    """
    if extension == 'json':
        return json.loads(string_data)
    elif extension in {'yaml', 'yml'}:
        return yaml.safe_load(string_data)
    raise RuntimeError('Unsupported extension')
