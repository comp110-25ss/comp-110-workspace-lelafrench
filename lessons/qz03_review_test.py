"""Review of unit tests - see lessons.qz03_review for functions"""

from lessons.qz03_review import (
    find_even,
    sum_numbers,
    is_prime,
    add_key_to_dicts,
    increment_dict_value,
    max_sum_dict,
)

# remember to specify use or edge case!


# 5
def test_find_even_use_case() -> None:
    """Test function find_even for use case"""
    nums: list[int] = [3, 7, 5, 3, 2]
    assert find_even(nums) == 4


# 6
def test_sum_numbers_use_case() -> None:
    """Test function sum_numbers for use case"""
    numbers: list[int] = [1, 4, 8]
    assert sum_numbers(numbers) == 13


# 7
def test_is_prime_use_case() -> None:
    """Test function is_prime for use case"""
    n: int = 7
    assert is_prime(n) is True


# 8
def test_aktd_use_case() -> None:
    """Test function add_key_to_dicts for use case"""
    dicts: list[dict] = [{"a": 1}, {"b": 2}]
    add_key_to_dicts(dicts, "c", 3)
    assert dicts == [{"a": 1, "c": 3}, {"b": 2, "c": 3}]


# 9
def test_idc_use_case() -> None:
    """Test function increment_dict_value for use case"""
    d: dict[str, int] = {"Lela": 21, "Leah": 20, "Miles": 18}
    increment_dict_value(d, "Lela")
    assert d["Lela"] == 22
    assert d["Leah"] == 20


# 10
def test_max_sum_dict_use_case() -> None:
    """Test function max_sum_dict for use case"""
    d: dict[str, list[int]] = {"Hi": [1, 2, 3], "Bye": [4, 5, 6]}
    assert max_sum_dict(d) == "Bye"
