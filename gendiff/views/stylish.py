"""Stylish output format module."""

import json
from typing import Any

from gendiff.tree import Node

INDENT = '    '
ADDED_INDENT = '  + '
REMOVED_INDENT = '  - '


def stringify_value(value: Any, depth: int = 1) -> str:
    if isinstance(value, dict):
        lines = ['{']
        for key, val in value.items():
            lines.append(
                '{0}{1}: {2}'.format(
                    INDENT * (depth + 1),
                    key,
                    stringify_value(val, depth + 1),
                )
            )
        lines.append('{0}}}'.format(INDENT * depth))
        return '\n'.join(lines)
    else:
        return value if isinstance(value, str) else json.dumps(value)


def stringify_node(name: str, node: Node, depth: int = 1) -> str:
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
            )
        )
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                ADDED_INDENT,
                name,
                stringify_value(node.children[1], depth),
            )
        )
    elif node.status == 'added':
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                ADDED_INDENT,
                name,
                stringify_value(node.children, depth),
            )
        )
    elif node.status == 'removed':
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                REMOVED_INDENT,
                name,
                stringify_value(node.children, depth),
            )
        )
    elif node.status == 'unchanged':
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                INDENT,
                name,
                stringify_value(node.children, depth),
            )
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
