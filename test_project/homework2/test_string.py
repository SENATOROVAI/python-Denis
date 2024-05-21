import pytest


class TestString:

    def test_slice_str(self):
        a = 'Hello '
        a = a[:1]
        assert a == 'H'


def test_multiply_str():
    a = 'Hello ' * 3
    assert len(a) == 18


@pytest.mark.parametrize('value', ['World', 'Is', 'Mine'])
def test_concatenation_str(value):
    a = 'Nice to meet you'
    a += value
    assert value in a


def test_upper_str():
    a = 'nice one'
    a = a.capitalize()
    assert a[:1] != 'n'


def test_comparing_str(random_value):
    a = '123'
    b = '1' + str(random_value)
    assert a < b
