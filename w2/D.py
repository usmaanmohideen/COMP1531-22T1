import pytest
from C import reverse_list, sum_list, minimum

https://www.tutorialspoint.com/pytest/pytest_fixtures.htm

@pytest.fixture
def lst():
    return [1, 2, 3]

@pytest.fixture
def lst2():

    return {
        'example 1': [6, 7, 8]
        'example 2': [5, 6, 7]
    }

def test_reverse(lst, lst2):
    reverse_list(lst)
    assert random_list == [3, 2, 1]

    reverse_list(lst2['example 2'])
    assert random_list == [8, 7, 6]


def test_min_positive(lst, lst2):
    assert minimum(lst) == 1
    assert minimum(lst2) == 6

def test_sum_positive(lst, lst2):
        assert sum_list(lst) == 6
        assert sum_list(lst2) == 21
