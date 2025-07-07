"""practicing conditionals"""


def check_first_letter(word: str, letter: str) -> str:
    """tells you if the first letter of word is the same as letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="hello", letter="h"))
print(check_first_letter(word="hello", letter="s"))
print(
    "complete"
)  # still goes back to the original program after the conditional is evaluated


def powerto(base: int, exp: int) -> int:
    if base == 0 or exp == 0:
        return 0
    else:
        return base**exp


print(powerto(base=2, exp=3))  # should return 8


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    else:
        return fibonacci(n - 1) + n


print(fibonacci(n=5))  # should return 5, as the sequence is 0, 1, 1, 2, 3, 5
