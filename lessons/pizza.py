"""Defining Pizza class to use in making_pizza.py"""


class Pizza:
    # attributes
    size: str  # small or large
    toppings: int
    gluten_free: bool

    # constructor
    def __init__(self, size_inp: str, toppings_inp: int, gluten_free_inp: bool):
        self.size = size_inp
        self.toppings = toppings_inp
        self.gluten_free = gluten_free_inp
        # returns self

    # methods
    def price(self) -> float:  # here it is a method
        """Calculate and return cost of pizza"""
        cost: float = 0.0
        if self.size == "large":  # charge for size
            cost += 6.0
        else:
            cost += 5.0
        cost += 0.75 * self.toppings  # 75 cents per topping
        if self.gluten_free:  # charge if GF
            cost += 1.0
        return cost

    def add_toppings(self, num_toppings: int) -> None:
        """Add a given number of toppings"""
        self.toppings += num_toppings


pie: Pizza = Pizza("medium", 2, False)  # creating new Pizza object
pie.add_toppings(2)
print(pie.price())
