from __future__ import (
    annotations,
)  # do this so we can call a Point within a Point method

"""Working with a new class called Point for CQ07."""

__author__: str = "730530237"


class Point:
    """Creating a new class called Point."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
        """Initializing a new Point object with x and y inputs."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Multiplying the object's x and y values by a given factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Instantiate a new Point based on the initial x and y values times factor."""
        new_point: Point = Point(
            (self.x * factor), (self.y * factor)
        )  # this was easier than one at a time defining
        return new_point

    def __str__(self) -> str:
        """Use a __str__ magic method to print a given object."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(
        self, factor: int
    ) -> Point:  # same function as scale method, just a magic method!
        """Instantiate a new Point by overloading the multiplication operator."""
        new_point: Point = Point((self.x * factor), (self.y * factor))
        return new_point

    def __add__(self, add_input: float) -> Point:
        """Instantiate a new Point by overloading the addition operator."""
        new_point: Point = Point(
            (self.x + add_input), (self.y + add_input)
        )  # add input to x and y
        return new_point
