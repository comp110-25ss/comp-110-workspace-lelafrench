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
