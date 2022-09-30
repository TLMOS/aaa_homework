import pytest

from morse import decode


@pytest.mark.parametrize(
    'encoded,expected',
    [
        ('... --- ...', 'SOS'),
        ('.- .- .-', 'AAA'),
        ('', ''),
        ('.... . .-.. .-.. --- .-- --- .-. .-.. -..', 'HELLOWORLD')
    ],
)
def test_encode(encoded, expected):
    actual = decode(encoded)
    assert actual == expected
