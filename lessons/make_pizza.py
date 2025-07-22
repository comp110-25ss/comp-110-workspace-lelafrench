"""Instantiating Pizza class from pizza.py"""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
your_pizza: Pizza = Pizza("small", 2, False)


# def price(pizza_order: Pizza) -> float: # here it's a function
#     """Calculate and return cost of pizza"""
#     cost: float = 0.0
#     if pizza_order.size == "large":  # charge for size
#         cost += 6.0
#     else:
#         cost += 5.0
#     cost += 0.75 * pizza_order.toppings  # 75 cents per topping
#     if pizza_order.gluten_free:  # charge if GF
#         cost += 1.0
#     return cost

print(my_pizza.toppings)
print(my_pizza.price())

# adding toppings
my_pizza.add_toppings(2)  # method with my_pizza as self, 2 as arg
print(my_pizza.toppings)
print(my_pizza.price())
