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
    for x, y, ttl in data:
        assert x + y == ttl


data = [
    [1, 2, 3],
    [-1, 1, 0],
    [0, 0, 0]
]


@pytest.mark.parametrize("x,y,ttl", data)
def test_sum_parameterized(x, y, ttl):
    assert x + y == ttl


@pytest.fixture(params=data)
def sum_arguments(request):
    return request.param[0], request.param[1], request.param[2]

def test_sum_simple(sum_arguments):
    x, y, ttl = sum_arguments
    assert x + y == ttl

def test_sum_keyword(sum_arguments):
    x, y, ttl = sum_arguments
    assert sum((x, y)) == ttl
