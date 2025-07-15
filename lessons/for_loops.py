"""Practicing for... in... loops."""

# basic setup of a for loop
pets: list[str] = ["Louie", "Bo", "Bear"]

for dogs in pets:
    print(f"Good boy, {dogs}!")


# figuring out how to use range backwards
num: list[int] = [2, 4, 6, 7]

for idx in range(len(num) - 1, -1, -1):
    print(num[idx])


# practicing range
names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
