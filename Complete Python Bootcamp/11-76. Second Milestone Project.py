import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'Cards in the deck:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands Dealer's Turn")
            playing = False
        else:
            print('Invalid input. Enter h or s only, please.')
            continue
        break


def show_some(player, dealer):

    print("DEALERS HAND:")
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print("PLAYER's HAND:")
    for card in player.cards:
        print(card)


def show_all(player, dealer):

    print("DEALER's HAND: ")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("PLAYER's HAND:")
    for card in player.cards:
        print(card)


def player_busts(player, dealer):
    print("BUST PLAYER")


def player_wins(player, dealer):
    print("PLAYER WINS")


def dealer_busts(player, dealer):
    print("PLAYER WINS! DEALER BUSTED!")


def dealer_wins(player, dealer):
    print("DEALER WINS! PLAYER BUSTED!")


def tie(player, dealer):
    print("DEALER AND PLAYER TIE! ")
