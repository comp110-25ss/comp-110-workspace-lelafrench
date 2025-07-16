"""Writing the function to be tested for CQ06 - unit test in max_test."""

__author__: str = "730530237"


def find_and_remove_max(input: list[int]) -> int:
    """Find, return, and remove the largest number in the input list."""
    if len(input) == 0:  # from example usage, if empty list then return -1
        return -1
    max: int = input[0]  # keep track of the max, starting at first value
    count: int = 0
    while count < len(input):
        if input[count] >= max:
            max = input[count]  # change max to current value
        count += 1
    count = 0
    while count < len(input):  # makes sure it removes every instance of the real max
        if input[count] == max:
            input.pop(count)
            count -= 1  # if something gets removed, even out the index
        count += 1
    return max  # can be returned since stored
