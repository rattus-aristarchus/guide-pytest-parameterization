import allure


def test_sum():
    x = 1
    y = 2
    ttl = 3
    allure.dynamic.parameter("x", x)
    allure.dynamic.parameter("y", y)
    allure.dynamic.parameter("sum", ttl)

    assert x + y == ttl
