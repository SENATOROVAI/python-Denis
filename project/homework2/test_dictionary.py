import pytest


class TestDict:

    def test_dict_generator(self):
        a = {n: n ** 2 for n in range(5)}
        b = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
        assert a == b


def test_get_dict_key():
    a = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    b = a.get(3)
    assert b == 9


@pytest.mark.parametrize("value", [2, 3, 4])
def test_pop_dict(value):
    a = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    a.pop(value)
    assert value not in a


def test_update_dict():
    a = {"name": "Bogdan"}
    b = {"age": "fifty"}
    a.update(b)
    c = {'name': 'Bogdan', 'age': 'fifty'}
    assert a == c


def test_addition_to_dict(random_value):
    a = {'name': 'Bogdan', "age": 'fifty'}
    a[random_value] = "text"
    assert random_value in a
