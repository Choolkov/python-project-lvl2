from pathlib import Path

from gendiff.parsing import parse_file
from gendiff.tree import build_tree

a = build_tree(
    parse_file(
        Path(
            '/home/square/hexlet/python-project-lvl2/tests/fixtures/file1.json'
        )
    ),
    parse_file(
        Path(
            '/home/square/hexlet/python-project-lvl2/tests/fixtures/file2.json'
        )
    ),
)
print(a)

{
    'common': Node(
        status='nested',
        children={
            'follow': Node(status='added', children=False),
            'setting1': Node(status='unchanged', children='Value 1'),
            'setting2': Node(status='removed', children=200),
            'setting3': Node(status='changed', children=(True, None)),
            'setting4': Node(status='added', children='blah blah'),
            'setting5': Node(status='added', children={'key5': 'value5'}),
            'setting6': Node(
                status='nested',
                children={
                    'doge': Node(
                        status='nested',
                        children={
                            'wow': Node(
                                status='changed', children=('', 'so much')
                            )
                        },
                    ),
                    'key': Node(status='unchanged', children='value'),
                    'ops': Node(status='added', children='vops'),
                },
            ),
        },
    ),
    'group1': Node(
        status='nested',
        children={
            'baz': Node(status='changed', children=('bas', 'bars')),
            'foo': Node(status='unchanged', children='bar'),
            'nest': Node(status='changed', children=({'key': 'value'}, 'str')),
        },
    ),
    'group2': Node(
        status='removed', children={'abc': 12345, 'deep': {'id': 45}}
    ),
    'group3': Node(
        status='added',
        children={'deep': {'id': {'number': 45}}, 'fee': 100500},
    ),
}
