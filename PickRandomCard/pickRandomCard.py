import random

cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


def pick_a_card():
    a = random.choices(cards)
    b = random.choices(ranks)

    print(f"The {a} of {b}")


pick_a_card()
