import pytest


class TestSet:

    def test_add_unique_value_to_set(self):
        s = {'a', 'b', 'c', 'd', "name", 5, -2, 0}
        s.add("new")
        assert "new" in s


def test_clear_set():
    s = {'a', 'b', 'c', 'd', "name", 5, -2, 0}
    s.clear()
    assert len(s) == 0


@pytest.mark.parametrize("value", [[], {}, {1: "one"}])
def test_add_unhashable_type_to_set(value):
    errors = []
    s = {'a', 'b', 'c', 'd', "name", 5, -2, 0}
    try:
        assert s.add(value)
    except TypeError:
        errors.append(f"unhashable type:{type(value)}")
    assert errors, "Errors list is empty"


def test_delete_element_from_set_by_another_set():
    s = {'a', 'b', 'c', 'd', "name", 5, -2, 0}
    b = {'e'}
    s.difference_update(b)
    assert b not in s


def test_len_set(random_value):
    s = {'a', 'b', 'c', 'd', "name", 5, -2, 0}
    assert len(s) > random_value
