import random
import time


class Cards:

    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol

    @staticmethod
    def deck_shuffle(deck, times):
        counter = 0
        while True:
            random.shuffle(deck)
            counter += 1
            if times == counter:
                break

    @staticmethod
    # we get the top card of the deck
    def card_draw(deck):
        card = popVal = deck.pop()
        return card

    # cards draw and flop, turn and river
    def hand_draw(self, deck):
        hand = [self.card_draw(deck), self.card_draw(deck)]
        return hand

    def flop_get(self, deck):
        flop = []
        count = 0
        for card in range(5):
            flop.append(self.card_draw(deck))
            count += 1
            # if count == 3:
            #     print(f'Flop : {self.show_cards(flop)}')
            # elif count == 4:
            #     time.sleep(2)
            #     print(f'River : {self.show_cards(flop)}')
            # elif count == 5:
            #     time.sleep(2)
            #     print(f'Turn : {self.show_cards(flop)}')
        print(self.show_cards(flop))
        return flop

    @staticmethod
    def show_cards(hand):

        translated = []
        count = 0

        for element in hand:
            count += 1

        for index in range(count):
            translated.append(hand[index].number + hand[index].symbol)

        return translated
