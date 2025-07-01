"""Challenge Question 00: Writing Functions"""

__author__ = "730530237"


def mimic(message: str) -> str:
    """take input and repeat it back"""
    return message


def main() -> None:
    """print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
