import random
import tkinter


# Function that loads the images
def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    for suit in suits:
        for card in range(1, 11):
            name = f'cards/{str(card)}_{suit}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        for card in face_cards:
            name = f'cards/{card}_{suit}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


# Dealing cards
def deal_card(frame):
    # Get the next card off the top of the deck
    next_card = deck.pop(0)
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list
    # Only one ace can have the value 11, and it will be reduced to 1
    # if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            card_value = 11
            ace = True
        score += card_value
    # If we would bust, check if there is an ace and substract 10
    if score > 21 and ace:
        score -= 10
        ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set('Dealer Wins!')
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set('Player Wins!')
    elif dealer_score > player_score:
        result_text.set('Dealer Wins!')
    else:
        result_text.set('Draw!')


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set('Dealer Wins!')


def new_game():
    global result_text
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    result_text.set('')
    new_frames()
    setup_game()


def setup_game():
    global deck
    global dealer_hand
    global player_hand
    # Create a new deck of cards and shuffle them
    deck = list(cards)
    random.shuffle(deck)

    # Create the list to store the dealer's hand and the player's hand
    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(dealer_hand[0][0])
    deal_player()


def new_frames():
    global dealer_card_frame
    global player_card_frame
    # Embedded frame to hold the dealer card images
    dealer_card_frame = tkinter.Frame(card_frame, background='SpringGreen3')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    # Embedded frame to hold the player card images
    player_card_frame = tkinter.Frame(card_frame, background='SpringGreen3')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)


# Setup of the screen and the frame for dealer and player
mainWindow = tkinter.Tk()
mainWindow.title('Blackjack')
mainWindow.geometry('640x480')
mainWindow.configure(background='SpringGreen3')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=1)

card_frame = tkinter.Frame(mainWindow, relief='sunken',
                           borderwidth=1, background='SpringGreen3')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='SpringGreen3',
              fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label,
              background='SpringGreen3', fg='white').grid(row=1, column=0)

new_frames()

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text='Player', background='SpringGreen3',
              fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label,
              background='SpringGreen3', fg='white').grid(row=3, column=0)

# Frame for the Buttons
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(
    button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(
    button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(
    button_frame, text='New Game', command=new_game)
new_game_button.grid(row=0, column=2)

# Loading cards
cards = []
load_images(cards)

setup_game()

mainWindow.mainloop()
