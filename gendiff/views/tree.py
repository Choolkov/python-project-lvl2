from gendiff.tree import Node

[
    Node(
        name='common',
        status='nested',
        value=[
            Node(name='follow', status='added', value=False),
            Node(name='setting1', status='unchanged', value='Value 1'),
            Node(name='setting2', status='removed', value=200),
            Node(name='setting3', status='changed', value=(True, None)),
            Node(name='setting4', status='added', value='blah blah'),
            Node(name='setting5', status='added', value={'key5': 'value5'}),
            Node(
                name='setting6',
                status='nested',
                value=[
                    Node(
                        name='doge',
                        status='nested',
                        value=[
                            Node(
                                name='wow',
                                status='changed',
                                value=('', 'so much'),
                            )
                        ],
                    ),
                    Node(name='key', status='unchanged', value='value'),
                    Node(name='ops', status='added', value='vops'),
                ],
            ),
        ],
    ),
    Node(
        name='group1',
        status='nested',
        value=[
            Node(name='baz', status='changed', value=('bas', 'bars')),
            Node(name='foo', status='unchanged', value='bar'),
            Node(
                name='nest', status='changed', value=({'key': 'value'}, 'str')
            ),
        ],
    ),
    Node(
        name='group2',
        status='removed',
        value={'abc': 12345, 'deep': {'id': 45}},
    ),
    Node(
        name='group3',
        status='added',
        value={'deep': {'id': {'number': 45}}, 'fee': 100500},
    ),
]
