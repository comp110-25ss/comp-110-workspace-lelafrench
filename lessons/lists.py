"""Practicing lists"""

from random import randint

# self-practice
grocery_list: list[str] = ["eggs", "milk", "bread"]
print(grocery_list)
print(grocery_list[0])
grocery_list[1] = "bananas"
print(grocery_list)
print(len(grocery_list))
grocery_list.append("milk")
grocery_list.pop(0)
print(grocery_list)

# video example
roll1: int = randint(1, 6)
roll2: int = randint(1, 6)
roll3: int = randint(1, 6)

dice_rolls: list[int] = [roll1, roll2, roll3]

dice_index: int = 0
dice_sum: int = 0
while dice_index <= len(dice_rolls) - 1:
    dice_sum += dice_rolls[dice_index]
    print(dice_rolls[dice_index])
    dice_index += 1
print(dice_sum)


a: int = 0
b: int = a
a += 10
print(b)

x: list[str] = ["comp", "110", "comp"]
print(x)
