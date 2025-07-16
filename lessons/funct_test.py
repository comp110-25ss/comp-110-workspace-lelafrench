"""Testing the functions from unit_tests.py"""

from lessons.unit_tests import get_first, remove_first, remove_and_get_first

# imported functions auto-update


# use cases
def test_get_first() -> None:  # use case
    """Testing basic behavior for get_first function"""
    assert get_first([4, 5, 6, 7]) == 4


def test_remove_first() -> None:  # trickier to test
    """Testing remove_first returns nothing"""
    a: list[int] = [4, 5, 6, 7]
    remove_first(a)
    assert a == [5, 6, 7]


def test_ragf() -> None:  # use case
    """Testing return and mutation for remove_and_get_first"""
    b: list[int] = [4, 5, 6, 7]
    remove_and_get_first(b)
    assert remove_and_get_first([4, 5, 6, 7]) == 4
    assert b == [5, 6, 7]


# edge cases
def test_get_first_edge() -> None:
    """Calling get_first on an empty list"""
    assert get_first([]) == -1


def test_remove_first_edge() -> None:
    """Calling remove_first on an empty list - should not do anything"""
    a: list[int] = []
    remove_first(a)
    assert a == []
