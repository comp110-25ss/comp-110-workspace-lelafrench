"""Practicing abstractions and algorithms in the contexts of lists."""

__author__: str = "730530237"


def all(big_list: list[int], same_int: int) -> bool:
    """Does the given int match every int in the list?"""
    count: int = 0
    if big_list == []:
        return False
    while count <= (len(big_list) - 1):
        if big_list[count] != same_int:
            return False
        count += 1
    return True  # only returns true if every int in list did not meet the if condition


def max(input: list[int]) -> int:
    """Find the max int in a list of ints."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    count: int = 0
    max_int: int = input[
        0
    ]  # define outside of loop because this is its initial assignment
    while count <= (len(input) - 1):
        current_int: int = input[
            count
        ]  # define within while loop so it changes with count
        if current_int > max_int:
            max_int = current_int  # reassign the value of max_int
        count += 1
    return max_int


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Is every value at every index equal in both lists?"""
    count: int = 0
    if len(list_1) != len(list_2):  # if they're not the same len, they're not equal
        return False
    while count <= (
        len(list_1) - 1
    ):  # could also use list_2 here since already matched the len
        if (
            list_1[count] != list_2[count]
        ):  # if even one int doesn't match, return False
            return False
        count += 1
    return True  # if every int passes thru while loop, return True


def extend(list_a: list[int], list_b: list[int]) -> None:
    """Add the values of one list to another list."""
    count: int = 0
    while count <= (
        len(list_b) - 1
    ):  # len of list b so no requirement that they're equal len
        list_a.append(
            list_b[count]
        )  # add one int at a time to heap, then when returned it will make one list
        count += 1
