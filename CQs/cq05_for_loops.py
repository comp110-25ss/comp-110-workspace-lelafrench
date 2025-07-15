"""Practice for-looping over lists and dicts."""

__author__: str = "730530237"

# Part 1


def w_sum(vals: list[float]) -> float:
    """Find the sum of a list using a while loop"""
    count: int = 0
    sum: float = 0.0
    while count < len(vals):
        sum += vals[count]
        count += 1
    if vals == []:  # ensuring an empty list returns 0.0
        sum = 0.0
    return sum


def f_sum(vals: list[float]) -> float:
    """Find the sum of a list using a for loop"""
    sum: float = 0.0
    for each_num in vals:
        sum += each_num  # this will add each value at of the list to sum
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Find the sum of a list using a for loop with range"""
    sum: float = 0.0
    for each_num in range(
        0, len(vals)
    ):  # end point is len(vals) so that the last index is included
        sum += vals[
            each_num
        ]  # range iterates over index - so to get value, use sub notation
    return sum


# Part 2


def get_keys(seq: dict[str, int]) -> list[str]:
    """Add the keys of a given dictionary to an empty list"""
    result: list[str] = []
    for keys in seq:
        result.append(keys)  # for loops iterate over the keys of a dictionary
    return result


def get_values(seq: dict[str, int]) -> list[int]:
    """Add the values of a given dictionary to an empty list"""
    result: list[int] = []
    for (
        values
    ) in (
        seq
    ):  # diff from get_keys b/c we don't want the key (auto-iterate), want its value
        result.append(
            seq[values]
        )  # collect the value of seq at each key using subscription notation
    return result
