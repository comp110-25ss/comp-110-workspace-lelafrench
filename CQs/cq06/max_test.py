"""Writing the unit tests for CQ06 - functions in find_max."""

__author__: str = "730530237"

from CQs.cq06.find_max import find_and_remove_max

# find_and_remove_max simplified to farm for space


def test_farm_return_use_case() -> None:
    """Ensure that find_and_remove_max returns the max value."""
    assert find_and_remove_max([16, 200, 16, 24]) == 200  # should return max value


def test_farm_mutate_use_case() -> None:
    """Ensure that find_and_remove_max mutates the input by removing max value."""
    a: list[int] = [40, 74, 125, 74, 125, 6]
    find_and_remove_max(a)
    assert a == [40, 74, 74, 6]


def test_farm_return_edge_case() -> None:
    """Ensure that find_and_remove_max returns the correct output in edge case"""
    assert find_and_remove_max([]) == -1
    # not sure what kind of error to == if you give the wrong iput type
