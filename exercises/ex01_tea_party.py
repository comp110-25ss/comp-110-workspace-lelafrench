"""Planning a tea party for me and my friends."""

__author__: str = "730530237"


def main_planner(guests: int) -> None:
    """Give a summary of our tea party preparations."""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # need to make each function call a str to concatenate
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $" + str(cost(tea_count=guests * 2, treat_count=guests * 3))
    )  # each guest will eat 3 treats (2 drinks * 1.5 treats/drink)


def tea_bags(people: int) -> int:
    """Calculating how many tea bags we'll need."""
    return people * 2


def treats(people: int) -> int:
    """Treats we need based on cups of tea drank."""
    return int(
        tea_bags(people=people) * 1.5
    )  # call number of drinks, multiply by treats per drink, make an int


def cost(tea_count: int, treat_count: int) -> float:
    """How much will our refreshments cost?"""
    return (tea_count * 0.50) + (treat_count * 0.75)  # sum the cost of tea and treats


if __name__ == "__main__":
    """Making the function runnable."""
    main_planner(guests=int(input("How many guests are attending your tea party?")))
