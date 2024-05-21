import pytest


class TestInt:

    def test_sum_int(self):
        a = 5
        b = 2
        assert a + b == 7


def test_division_int():
    a = 356
    b = 4
    assert a // b == 89


@pytest.mark.parametrize("value", ['love', [], {}, {1: "one"}])
def test_add_unhashable_type_to_int(value):
    errors = []
    a = 5
    try:
        assert a + value
    except TypeError:
        errors.append(f"unhashable type:{type(value)}")
    assert errors, "Errors list is empty"


def test_subtraction_int():
    a = 1024
    b = 5000
    assert a - b == -3976


def test_division_int_type(random_value):
    a = 1024
    b = 5
    c = a / b
    assert type(c) != type(int)
    assert c == 204.8
