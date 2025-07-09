"""Creating a Wordle-type game for guessing a mystery word."""

__author__: str = "730530237"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    while turns <= 6:  # needs to be <= 6 so it gives sixth turn
        print("=== Turn " + str(turns) + "/6 ===")
        guess = input_guess(
            expected_length=len(secret)
        )  # ask for the guess and store it here
        print(
            emojified(guess_word=guess, secret_word=secret)
        )  # so that the guess can be evaluated here
        if guess == secret:  # if you win
            print("You won in " + str(turns) + "/6 turns!")
            return None  # need this so the function exits if you win
        elif turns == 6:  # if you lose
            print("X/6 - Sorry, try again tomorrow!")
        turns = turns + 1


def contains_char(word: str, search_char: str) -> bool:
    """To see if the search character is in the guess word - yellow blocks."""
    assert len(search_char) == 1, f"len('{search_char}') is not 1"
    char_index: int = 0
    while char_index < len(word):
        if word[char_index] == search_char:
            return True  # if any of the characters match, returns True and exits
        char_index = char_index + 1
    return False  # if the entire code runs without a return, then the return is False


white_box: str = "\U00002b1c"
green_box: str = "\U0001f7e9"
yellow_box: str = "\U0001f7e8"


def emojified(guess_word: str, secret_word: str) -> str:
    """Gives emojis to describe how close the guess word is to the secret word."""
    assert len(guess_word) == len(
        secret_word
    ), "Guess must be the same length as secret"
    char_index: int = 0
    answer: str = ""
    while char_index < len(secret_word):  # could use either guess or secret word
        if (
            guess_word[char_index] == secret_word[char_index]
        ):  # if the guess character matches secret character
            answer = answer + green_box
        elif contains_char(
            word=secret_word, search_char=guess_word[char_index]
        ):  # if guess char matches some secret char - if contain_char returns True
            answer = answer + yellow_box
        else:  # if nothing matches - if contain_char returns False
            answer = answer + white_box
        char_index = char_index + 1
    return answer


def input_guess(expected_length: int) -> str:
    """Makes sure the user makes a guess of the correct length"""
    user_input: str = input(
        "Enter a " + str(expected_length) + " character word:"
    )  # define this so we can change the input question
    while len(user_input) != expected_length:
        user_input = input(
            "That wasn't " + str(expected_length) + " chars! Try again:"
        )  # run another input function until length is correct
    return user_input


if __name__ == "__main__":
    main(secret="codes")  # can change the secret word here
