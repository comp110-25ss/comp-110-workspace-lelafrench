"""Practicing while loops for counting character instances in a string."""

__author__ = "730530237"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # number of times search_char appears in phrase
    char_index: int = 0  # which character in phrase is being checked
    while char_index < len(phrase):
        if (
            phrase[char_index] == search_char
        ):  # check if each character is same as search_char
            count = count + 1  # if it is the same, increase the count
        char_index = (
            char_index + 1
        )  # no matter if it's the same, increase the index to move on
    return count
