"""Stylish output format module."""

import json
from typing import Any

from gendiff.tree import Node

INDENT = '    '
ADDED_INDENT = '  + '
REMOVED_INDENT = '  - '
status_indents = {
    'added': ADDED_INDENT,
    'removed': REMOVED_INDENT,
    'unchanged': INDENT,
}


def stringify_value(node_value: Any, depth: int = 1) -> str:
    """
    Return a string representation of the value.

    Args:
        node_value: value
        depth: indent depth

    Returns:
        str
    """
    if isinstance(node_value, dict):
        lines = ['{']
        for subkey, subvalue in node_value.items():
            lines.append(
                '{0}{1}: {2}'.format(
                    INDENT * (depth + 1),
                    subkey,
                    stringify_value(subvalue, depth + 1),
                ),
            )
        lines.append('{0}}}'.format(INDENT * depth))
        return '\n'.join(lines)
    return (
        node_value
        if isinstance(node_value, str)
        else json.dumps(node_value)
    )


def stringify_node(name: str, node: Node, depth: int = 1) -> str:
    """
    Return a string representation of the node.

    Args:
        name: name of node
        node: node
        depth: indent depth

    Returns:
        str
    """
    lines = []
    if node.status == 'nested':
        lines.append('{0}{1}: {{'.format(INDENT * depth, name))
        for child_name, child_node in node.children.items():
            lines.append(stringify_node(child_name, child_node, depth + 1))
        lines.append('{0}}}'.format(INDENT * depth))
    elif node.status == 'changed':
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                REMOVED_INDENT,
                name,
                stringify_value(node.children[0], depth),
            ),
        )
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                ADDED_INDENT,
                name,
                stringify_value(node.children[1], depth),
            ),
        )
    elif node.status in {'added', 'removed', 'unchanged'}:
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                status_indents[node.status],
                name,
                stringify_value(node.children, depth),
            ),
        )

    return '\n'.join(lines)


def get_stylish(tree: dict) -> str:
    """
    Return a stylish representation of the diff tree.

    Args:
        tree: diff tree

    Returns:
        str
    """
    lines = ['{']
    for name, node in tree.items():
        lines.append(stringify_node(name, node))
    lines.append('}')
    return '\n'.join(lines)
