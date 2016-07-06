import ujson


def slow_fib(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    a = slow_fib(n-1)
    b = slow_fib(n-2)
    return a + b


def fast_fib(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(n-2):
        a, b = b, a + b
    return a + b


def decode(json_string):
    return ujson.loads(json_string)
