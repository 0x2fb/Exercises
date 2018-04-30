import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.points = self.get_points(value)

    def __repr__(self):
        return f'{self.value} of {self.suit}'

    def get_points(self, value):
        p_cards = ['J', 'Q', 'K']
        try:
            v = int(value)
        except ValueError:
            if value in p_cards:
                v = 10
            elif value == "A":
                v = 11
        return v


class Deck:

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spaces')
    values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self):
        self.cards = [Card(i, j) for j in Deck.values for i in Deck.suits]

    def __repr__(self):
        return f'There are {self.count()} in the deck.'

    def __iter__(self):
        for card in self.cards:
            yield card

    def count(self):
        return len(self.cards)

    def _deal(self, rem_cards):
        if rem_cards <= self.count():
            return [self.cards.pop() for n in range(rem_cards)]
        else:
            raise ValueError("Not enough cards left.")

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError('Only full decks can be shuffled.')

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number):
        return self._deal(number)
