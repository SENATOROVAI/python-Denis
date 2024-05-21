import pytest
import random


@pytest.fixture
def random_value():
    return random.randrange(3, 5)
