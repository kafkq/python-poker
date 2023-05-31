from Cards import Cards
from Rules import Rules
from Winner import Winner
import random

num = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
sym = ("♣", "♦", "♥", "♠")
deck = []

card = Cards("Builder", "Main")
rules = Rules("Poker")

play = True


def deck_make():
    deck.clear()
    for x in num:
        for y in sym:
            deck.append(Cards(x, y))


deck_make()
card.deck_shuffle(deck, 2)

hand_1 = card.hand_draw(deck)
hand_2 = card.hand_draw(deck)


print(f'Player 1 : {card.show_cards(hand_1)}   |   Player 2 : {card.show_cards(hand_2)}\n')

flop = card.flop_get(deck)

check = Winner("poker")

# print(check.check_high_card(hand_1, hand_2, flop))
print(check.check_pairs(hand_1,hand_2, flop))



