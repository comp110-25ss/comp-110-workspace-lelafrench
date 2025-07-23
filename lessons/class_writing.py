from __future__ import annotations

"""Practicing class writing for final exam."""

"""Function and method writing with class objects."""


class Course:
    """models the idea of a UNC course."""

    name: str
    level: int
    prerequisites: list[str]

    # 2
    def is_valid_course(self, course: str) -> bool:
        if self.level >= 400:
            for c in self.prerequisites:
                if c == course:
                    return True
        return False


# 1
def find_courses(catalog: list[Course], search: str) -> list[str]:
    course_list: list[str] = []
    for classes in catalog:
        if classes.level >= 400:
            for c in classes.prerequisites:
                if c == search:
                    course_list.append(classes.name)
    return course_list


"""Class writing."""


# 1
class Car:
    """Creating a new class called Car."""

    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(
        self,
        make_inp: str,
        model_inp: str,
        year_inp: int,
        color_inp: str,
        mileage_inp: float,
    ):
        """Initialize a new Car object using given inputs."""
        self.make = make_inp
        self.model = model_inp
        self.year = year_inp
        self.color = color_inp
        self.mileage = mileage_inp

    def update_mileage(self, miles: float):
        """Updating the car's mileage for a given input."""
        self.mileage += miles

    def display_info(self):
        print("--Car Information:--")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage}")


def calculate_depreciation(car: Car, depreciation_rate: float) -> float:
    return car.mileage * depreciation_rate


my_car: Car = Car("Toyota", "Avalon", 2015, "Blue", 47000.0)
my_car.update_mileage(2000.0)
my_car.display_info()

print(calculate_depreciation(my_car, 0.5))


"""Class writing and magic methods."""


class HotCocoa:
    """Defining a new class called HotCocoa."""

    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, whip: bool, flavor: str, mallows: int, sweetness: int):
        self.has_whip = whip
        self.flavor = flavor
        self.marshmallow_count = mallows
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int):
        self.marshmallow_count += mallows
        self.sweetness *= mallows * 2

    def __str__(self) -> str:
        if self.has_whip:
            return (
                f"{self.flavor} Wcocoa, {self.marshmallow_count} Ms, {self.sweetness}S."
            )
        else:
            return (
                f"{self.flavor} cocoa, {self.marshmallow_count} Ms, {self.sweetness}S."
            )


def order_cost(order: list[HotCocoa]) -> float:
    total_cost: float = 0.0
    for drink in order:
        if drink.has_whip:
            total_cost += 2.5
        else:
            total_cost += 2.0
    return total_cost


my_order: HotCocoa = HotCocoa(False, "vanilla", 5, 2)
my_order.has_whip = True
my_order.mallow_adder(2)

your_order: HotCocoa = HotCocoa(True, "peppermint", 10, 2)
order_cost([my_order, your_order])
print(my_order)


class TimeSpent:
    """Defining a new class called TimeSpent."""

    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        """Initialize a TimeSpent object."""
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, time: int):
        """Add time to an object's minutes."""
        self.minutes += time

    def __add__(self, added_minutes: int) -> TimeSpent:
        """New object with the added time."""
        new_object = self
        new_object.minutes += added_minutes
        return new_object

    def reset(self) -> int:
        """Reset the object's minutes and return the old minutes."""
        old_minutes: int = self.minutes
        self.minutes = 0
        return old_minutes

    def __str__(self) -> str:
        """Turn object attributes into a string."""
        mins: int = self.minutes % 60
        hours: float = (self.minutes - mins) / 60
        return (
            f"{self.name} has spent {hours} hours and {mins} minutes on {self.purpose}."
        )


def most_by_purpose(inp: list[TimeSpent], purpose: str) -> str:
    """Who spent the most time doing the given activity?"""
    max_time: int = 0
    max_name: str = ""
    for person in inp:
        if person.purpose == purpose and person.minutes > max_time:
            person.name = max_name
            person.minutes = max_time
    return max_name
