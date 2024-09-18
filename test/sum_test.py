import allure
import pytest


def test_sum():
    assert 1 + 2 == 3


def test_sum_loop():
    data = [
        [1, 2, 3],
        [-1, 1, 0],
        [0, 0, 0]
    ]
    for term_0, term_1, sum in data:
        assert term_0 + term_1 == sum


data = [
    [1, 2, 3],
    [-1, 1, 0],
    [0, 0, 0]
]


@pytest.mark.parametrize("term_0,term_1,sum", data)
def test_sum_parameterized(term_0, term_1, sum):
    assert term_0 + term_1 == sum
