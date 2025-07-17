"""Practicing writing functions to review for Quiz 3"""

"""Lists"""


# 1
def odd_and_even(nums: list[int]) -> list[int]:
    """Find and return the odd values with even indexes"""
    count: int = 0
    result: list[int] = []
    while count < len(nums):
        if nums[count] % 2 == 1 and count % 2 == 0:
            result.append(nums[count])
        count += 1
    return result


# 2
def short_words(words: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters"""
    count: int = 0
    result: list[str] = []
    while count < len(words):
        if len(words[count]) >= 5:
            print(f"{words[count]} is too long!")
        elif len(words[count]) < 5:
            result.append(words[count])
        count += 1
    return result


# 3
def multiples(list1: list[int]) -> list[bool]:
    """See if the previous value is a multiple of the current value"""
    count: int = 0
    result: list[bool] = []
    while count < len(list1):
        if count == 0:
            if list1[count] % list1[len(list1) - 1] == 0:
                result.append(True)
            else:
                result.append(False)
        if count > 0:
            if list1[count] % list1[count - 1] == 0:
                result.append(True)
            else:
                result.append(False)
        count += 1
    return result


# 4
def reverse_multiply(list1: list[int]) -> list[int]:
    """Reverse and double list elements"""
    result: list[int] = []
    count: int = len(list1) - 1
    while count >= 0:
        result.append(list1[count] * 2)
        count -= 1
    return result


"""Dictionaries"""


# 1
def value_exists(d: dict[str, int], num: int) -> bool:
    for x in d:
        if d[x] == num:
            return True
    return False


# 2
def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] += n
        elif inp[key] % 2 == 1:
            inp[key] -= n


# 3
def free_biscuits(result: dict[str, list[int]]) -> dict[str, bool]:
    biscuit: dict[str, bool] = {}
    for x in result:
        if sum(result[x]) >= 100:
            biscuit[x] = True
        else:
            biscuit[x] = False
    return biscuit
