"""Mutating functions."""

__author__: str = "730530237"


def manual_append(mutated: list[int], num: int) -> None:
    mutated.append(num)
    return None


def double(base_list: list[int]) -> None:
    count: int = 0
    while count <= (len(base_list) - 1):
        base_list[count] *= 2
        count += 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
