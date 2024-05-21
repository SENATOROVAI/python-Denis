import pytest


class TestList:

    def test_len_list_after_multiplication(self):
        lis = [2, 4, [], {}, "heh"] * 2
        assert len(lis) == 10


def test_list_after_clear():
    lis = [2, 4, [], {}, "heh"]
    lis.clear()
    assert lis == []


@pytest.mark.parametrize("value", [4, {}, "heh"])
def test_remove_elements_from_list_by_value(value):
    lis = [2, 4, [], {}, "heh"]
    lis.remove(value)
    assert value not in lis


def test_remove_element_from_list_by_index():
    lis = [2, 4, [], {}, "heh"]
    lis.pop(4)
    assert lis[-1] != "heh"


def test_list(random_value):
    lis = [2, 4, [], {}, "heh"]
    lis.insert(1, random_value)
    assert random_value in lis
