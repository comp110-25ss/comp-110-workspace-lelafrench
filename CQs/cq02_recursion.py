"""Challenge question to practice recursions."""

__author__ = "730530237"


def f(n: int, k: int) -> int:
    if n == 0:
        return 0
    else:
        return f(n - 1, k) + k
