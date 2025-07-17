"""Practicing dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

ice_cream["mint"] = 15
ice_cream.pop("chocolate")

print(ice_cream)
print(f"{ice_cream['vanilla']} people ordered vanilla")

while ice_cream["strawberry"] <= 7:
    print(f"{ice_cream['strawberry']} people ordered strawberry")
    ice_cream["strawberry"] += 1

print("mango" in ice_cream)

test: dict[str, str] = {"Hi": "does", "this": "work?"}
print(test)


quiz_review: dict[str, int] = {"Hello": 4, "COMP": 110, "Bye": 8}

q2: dict[str, int] = {"Hi": quiz_review["Hello"]}
