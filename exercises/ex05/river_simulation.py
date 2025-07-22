"""Creating a river ecosystem using OOP."""

__author__: str = "730530237"

from exercises.ex05.river import River

my_river: River = River(10, 2)  # starting a new River instance
print(my_river.view_river())  # get an idea of the River

print(my_river.one_river_week())  # see what the River looks like after a week

my_river.remove_fish(1)  # take away a Fish
print(my_river.view_river())  # and see what that does
