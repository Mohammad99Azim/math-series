def fibonacci(n: int):
    if type(n) != type(1):
        return "Integer Values only"
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n: int):
    if type(n) != type(1):
        return "Integer Values only"
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
