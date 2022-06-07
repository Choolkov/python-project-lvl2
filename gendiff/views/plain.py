"""Plain output format module."""

import json
from typing import Any

from gendiff.tree import Node


def stringify_value(node_value: Any) -> str:
    """
    Return string of value.

    Args:
        node_value: value

    Returns:
        str
    """
    if isinstance(node_value, dict):
        return '[complex value]'
    return (
        "'{0}'".format(node_value)
        if isinstance(node_value, str)
        else json.dumps(node_value)
    )


def stringify_node(name: str, node: Node) -> str:  # NOQA WPS231
    lines = []
    if node.type == 'nested':
        for child_name, child_node in node.value.items():
            child_name = '{0}.{1}'.format(name, child_name)
            lines.append(stringify_node(child_name, child_node))
    elif node.type == 'changed':
        lines.append(
            "Property '{0}' was updated. From {1} to {2}".format(
                name,
                stringify_value(node.value[0]),
                stringify_value(node.value[1]),
            ),
        )
    elif node.type == 'added':
        lines.append(
            "Property '{0}' was added with value: {1}".format(
                name, stringify_value(node.value),
            ),
        )
    elif node.type == 'removed':
        lines.append("Property '{0}' was removed".format(name))
    return '\n'.join(filter(None, lines))


def get_plain(tree: dict) -> str:
    """
    Return a string representation of the diff tree.

    Args:
        tree: diff tree

    Returns:
        str
    """
    lines = []
    for name, node in tree.items():
        lines.append(stringify_node(name, node))
    return '\n'.join(filter(None, lines))
