"""Video lecture's example of unit tests."""


def get_first(input: list[int]) -> int:
    """Return the first element (index 0) of the input list"""
    if len(input) == 0:  # list should have at least one element
        return -1
    return input[0]


def remove_first(input: list[int]) -> None:
    """Remove the first element (idx 0) of the input list"""
    if len(input) > 0:  # added to ensure edge case works
        input.pop(0)


def remove_and_get_first(input: list[int]) -> int:
    """Remove AND return the first element of the input list"""
    first: int = input[0]
    input.pop(0)
    return first


# How do we edit and test these functions w/o restarting python REPL? -> unit test!
