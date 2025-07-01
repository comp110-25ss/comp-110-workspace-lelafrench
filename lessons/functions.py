"""practice for LS04, writing and calling functions"""


def sum(num1: int, num2: int) -> int:
    """takes two ints and returns sum"""
    return num1 + num2


print(sum(num1=11, num2=3))


def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))


def total_cost(price: int, tax_rate: float) -> float:
    return price + (price * tax_rate)


print(total_cost(price=100, tax_rate=0.07))


def returning(word: str) -> str:
    return word


def echo(word: str, times: int) -> str:
    return returning(word=word) * times


print(echo(word="hello", times=4))


def have_done(task, completed) -> str:
    return "Completed " + task + ": " + str(completed)


print(have_done(task="homework", completed=False))


def greet(name: str) -> str:
    return "I'm so happy to see you " + name + "!"
    print(
        "Hello "
        + name
        + ", your name starts with an "
        + name[0]
        + " and ends with an "
        + name[len(name) - 1]
    )


def main() -> None:
    print(greet(name="Molly"))


main()


def get_starting_point(word: str) -> int:
    return int(len(word) / 3)


print(get_starting_point(word="mystery"))
