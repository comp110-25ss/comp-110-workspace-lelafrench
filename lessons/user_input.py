"""Practice user input, elif, and variable assignment."""

forecast: str = input("What is the weather?")
forecast = input(
    "Double checking... what is the weather?"
)  # overwrites the previous value of forecast
hot_day: str = "sunny"
if forecast == "rainy":
    print("Bring an umbrella!")
else:
    if forecast == hot_day:  # could also be forecast == "sunny"
        print("Wear sunglasses!")
    else:
        print("You're out of luck.")

forecast: str = input("What is the weather?")
if forecast == "rainy":
    print("Bring an umbrella!")
elif forecast == "sunny":
    print("Wear sunglasses!")
else:  # everything gets unindented
    print("You're out of luck.")


age: int = 10
age = age + 1
print(age)
