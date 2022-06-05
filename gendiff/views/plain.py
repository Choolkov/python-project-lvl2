"""Plain output format module."""

import json
from typing import Any

from gendiff.tree import Node


def stringify_value(value: Any) -> str:
    if isinstance(value, dict):
        return '[complex value]'
    return (
        "'{0}'".format(value) if isinstance(value, str) else json.dumps(value)
    )


def stringify_node(node: Node) -> str:
    lines = []
    if node.status == 'nested':
        for child in node.values:
            child_node = Node(
                '{0}.{1}'.format(node.name, child.name),
                child.status,
                child.values,
            )
            lines.append(stringify_node(child_node))
    elif node.status == 'changed':
        lines.append(
            "Property '{0}' was updated. From {1} to {2}".format(
                node.name,
                stringify_value(node.values[0]),
                stringify_value(node.values[1]),
            )
        )
    elif node.status == 'added':
        lines.append(
            "Property '{0}' was added with value: {1}".format(
                node.name, stringify_value(node.values)
            )
        )
    elif node.status == 'removed':
        lines.append("Property '{0}' was removed".format(node.name))
    return '\n'.join(filter(None, lines))


def get_plain(tree: list) -> str:
    lines = []
    for node in tree:
        lines.append(stringify_node(node))
    print('\n'.join(lines))
    return '\n'.join(filter(None, lines))
