from series import fibonacci, lucas, sum_series


def test_fibonacci_one():
    assert fibonacci(0) == 0


def test_fibonacci_two():
    assert fibonacci(1) == 1


def test_fibonacci_three():
    assert fibonacci(2) == 1


def test_fibonacci_four():
    assert fibonacci(3) == 2


def test_fibonacci_five():
    assert fibonacci(7) == 13


def test_fibonacci_six():
    assert fibonacci(23) == 28657


def test_fibonacci_seven():
    assert fibonacci('str') == "Integer Values only"


def test_lucas_one():
    assert lucas(0) == 2


def test_lucas_two():
    assert lucas(1) == 1


def test_lucas_three():
    assert lucas(2) == 3


def test_lucas_four():
    assert lucas(3) == 4


def test_lucas_five():
    assert lucas(7) == 29


def test_lucas_six():
    assert lucas(23) == 64079


def test_lucas_seven():
    assert lucas('str') == "Integer Values only"


def test_sum_series_one():
    assert sum_series(0, 2, 1) == 2


def test_sum_series_two():
    assert sum_series(1, 2, 1) == 1


def test_sum_series_three():
    assert sum_series(2, 2, 1) == 3


def test_sum_series_four():
    assert sum_series(3, 2, 1) == 4


def test_sum_series_five():
    assert sum_series(7, 2, 1) == 29


def test_sum_series_six():
    assert sum_series(23, 2, 1) == 64079


def test_sum_series_one_2p():
    assert sum_series(0, 0, 1) == 0


def test_sum_series_two_2p():
    assert sum_series(1, 0, 1) == 1


def test_sum_series_three_2p():
    assert sum_series(2, 0, 1) == 1


def test_sum_series_four_2p():
    assert sum_series(3, 0, 1) == 2


def test_sum_series_five_2p():
    assert sum_series(7, 0, 1) == 13


def test_sum_series_six_2p():
    assert sum_series(23, 0, 1) == 28657
