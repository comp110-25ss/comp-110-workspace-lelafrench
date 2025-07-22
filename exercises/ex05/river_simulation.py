"""Creating a river ecosystem using OOP."""

__author__: str = "730530237"

from exercises.ex05.river import River

my_river: River = River(10, 2)
print(my_river.view_river())

print(my_river.one_river_week())

my_river.remove_fish(1)
print(my_river.view_river())
