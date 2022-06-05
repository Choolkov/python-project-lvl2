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


def stringify_node(node: Node, depth: int = 1) -> str:
    lines = []

    if node.status == 'nested':
        lines.append('{0}{1}: {{'.format(INDENT * depth, node.name))
        for value in node.values:
            lines.append(stringify_node(value, depth + 1))
        lines.append('{0}}}'.format(INDENT * depth))
    elif node.status == 'changed':
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                REMOVED_INDENT,
                node.name,
                stringify_value(node.values[0], depth),
            )
        )
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                ADDED_INDENT,
                node.name,
                stringify_value(node.values[1], depth),
            )
        )
    elif node.status == 'added':
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                ADDED_INDENT,
                node.name,
                stringify_value(node.values, depth),
            )
        )
    elif node.status == 'removed':
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                REMOVED_INDENT,
                node.name,
                stringify_value(node.values, depth),
            )
        )
    elif node.status == 'unchanged':
        lines.append(
            '{0}{1}{2}: {3}'.format(
                INDENT * (depth - 1),
                INDENT,
                node.name,
                stringify_value(node.values, depth),
            )
        )

    return '\n'.join(lines)


def get_stylish(tree: list) -> str:
    lines = ['{']
    for node in tree:
        lines.append(stringify_node(node))
    lines.append('}')
    return '\n'.join(lines)
