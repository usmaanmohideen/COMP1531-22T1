import pytest

@pytest.fixture
def lst():
    return [1, 2, 3, 4, 5]

def test_reverse(lst):
    reverse_list(l)
    assert l == [5, 4, 3, 2, 1]

def test_min_positive(lst):
    assert minimum(lst) == 1

def test_sum_positive(lst):
    assert sum_list(lst) == 15
