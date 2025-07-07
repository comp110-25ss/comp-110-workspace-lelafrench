"""Demonstrates while loops by finding low value in string."""

cards: str = "5235"  # need to use a str becuase we can't index an int

# look at each number in the string using index
card_index: int = 0
low_card: int = int(cards[0])

while card_index < 4:
    # check if current card is less than low card
    current_card: int = int(
        cards[card_index]
    )  # since this is always changing, define in the while loop
    if current_card < low_card:
        # update the low card to be the value of our current card
        low_card = current_card
    card_index = card_index + 1

print(low_card)
