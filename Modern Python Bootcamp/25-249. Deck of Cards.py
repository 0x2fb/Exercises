import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spaces')
    values = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self):
        self.cards = [Card(i, j) for j in Deck.values for i in Deck.suits]

    def __repr__(self):
        return f'There are {self.count()} in the deck.'

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


test_deck = Deck()
print(test_deck)
print(test_deck.cards)
test_deck.shuffle()
print(test_deck.cards)
print(test_deck.deal_card())
print(test_deck.deal_hand(5))
test_deck.count()
