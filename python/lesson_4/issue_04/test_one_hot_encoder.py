import pytest

from one_hot_encoder import fit_transform


@pytest.mark.parametrize(
    'doc,expected',
    [
        ('Apple', [
            ('Apple', [1])
        ]),
        (['Apple', 'Bee', 'Apple', 'Tree'], [
            ('Apple', [0, 0, 1]),
            ('Bee',   [0, 1, 0]),
            ('Apple', [0, 0, 1]),
            ('Tree',  [1, 0, 0])
        ])
    ],
)
def test_default(doc, expected):
    transformed = fit_transform(doc)
    assert transformed == expected


def test_args():
    doc = ['Apple', 'Bee']
    expected = [
        ('Apple', [0, 1]),
        ('Bee',   [1, 0])
    ]
    transformed = fit_transform(*doc)
    assert transformed == expected


def test_case_sensetivity():
    doc = ['Apple', 'apple', 'aPple']
    transformed = fit_transform(doc)
    assert 'appLE' not in transformed


def test_zero_args():
    with pytest.raises(TypeError):
        fit_transform()
