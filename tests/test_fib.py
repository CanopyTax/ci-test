import pytest

from source.core import slow_fib, fast_fib

slow_test_data = [
    (-100, 0),
    (-10, 0),
    (-1, 0),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (15, 610),
    (20, 6765),
]

fast_test_data = [(i, slow_fib(i)) for i in range(-5, 30)]
fast_test_data += [  # this stuff wont work on slow
    (50, 12586269025),
    (75, 2111485077978050),
    (100, 354224848179261915075),
    (199, 173402521172797813159685037284371942044301),
]


@pytest.mark.parametrize('in_, expected', slow_test_data)
def test_slow_fib(in_, expected):
    assert slow_fib(in_) == expected


@pytest.mark.parametrize('in_, expected', fast_test_data)
def test_fast_fib(in_, expected):
    assert fast_fib(in_) == expected
