"""Review of dictionaries"""

# 11
my_dictionary: dict[str, float] = dict()

# 12
msg: dict[str, int] = {"Hello": 1, "Yall": 2}
msg["Yall"]

# 13
msg["Yall"] += 3

# 14
ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
len(ids)

# 15
inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}
inventory["markers"] = 15

# 16
prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}
prices["milk"] = 2.50

# 17
scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
for x in scores:
    print(x)


# 18
def sum(inp_dict: dict[str, int]) -> int:
    total_score: int = 0
    for x in inp_dict:
        total_score += inp_dict[x]
    return total_score


tot_score = sum(scores)
tot_score2 = sum(inp_dict=scores)

# 19
fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}
for f in fruit_count:
    print(f"{f}: {fruit_count[f]}")

# 20
first_dict: dict[str, int] = {"a": 1, "b": 2}
second_dict: dict[str, int] = {"c": 3, "d": 4}

combo_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4}


"""Review of for loops"""

# 1.1
stats: list[int] = [7, 8, 9]
total: int = 100
for nums in stats:
    total -= nums  # for loop iterates thru values

# 1.2
total2: int = 100
for x in range(0, len(stats)):
    total2 -= stats[x]  # for loop with range iterates thru keys/indeces


"""Review of unit tests - see lessons.qz03_review_test for tests"""


# 5
def find_even(nums: list[int]) -> int:
    """See if any value in a list is even, and return its index"""
    idx: int = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            return idx
        idx += 1
    return -1


# 6
def sum_numbers(numbers: list[int]) -> int:
    """Sum a list of numbers"""
    if len(numbers) == 0:
        raise Exception("Empty list - no elements to add")
    total: int = numbers[0]
    for i in range(1, len(numbers)):
        total += numbers[i]
    return total


# 7
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 8
def add_key_to_dicts(dicts: list[dict], key: str, value: int) -> None:
    """Add a key to a dictionary"""
    for d in dicts:
        d[key] = value


# 9
def increment_dict_value(d: dict[str, int], key: str) -> None:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


# 10
def max_sum_dict(d: dict[str, list[int]]) -> str:
    """Sum dict elements and return key with largest summed value"""
    keys = []
    for key in d:
        keys.append(key)
    values_list_1 = d[keys[0]]
    values_list_2 = d[keys[1]]
    total_1 = 0
    for value in values_list_1:
        total_1 += value
    total_2 = 0
    for value in values_list_2:
        total_2 += value
    if total_1 > total_2:
        return keys[0]
    else:
        return keys[1]
