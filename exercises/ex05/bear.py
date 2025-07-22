"""File to define Bear class."""

__author__: str = "730530237"


class Bear:
    """Create a new class called Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a new Bear object."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increase age and hunger and decrease hunger score daily."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increase a Bear's hunger score when it eats a Fish."""
        self.hunger_score += num_fish
