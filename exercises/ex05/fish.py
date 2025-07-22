"""File to define Fish class."""

__author__: str = "730530237"


class Fish:
    """Define a new class called Fish."""

    age: int

    def __init__(self):
        """Initialize a new Fish object."""
        self.age = 0
        return None

    def one_day(self):
        """Add a day to a Fish's age."""
        self.age += 1
        return None
