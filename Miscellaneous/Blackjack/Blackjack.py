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
    next_card = deck.pop()
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief ='raised').pack(side='left')
    # now return the card's face value
    return next_card

def deal_dealer():
    deal_card(dealer_card_frame)

def deal_player():
    deal_card(player_card_frame)



# Setup of the screen and the frame for dealer and player
mainWindow = tkinter.Tk()
mainWindow.title('Blackjack')
mainWindow.geometry('640x480')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=1)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='SpringGreen3')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='SpringGreen3', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='SpringGreen3', fg='white').grid(row=1, column=0)

# Embedded frame to hold the dealer card images
dealer_card_frame = tkinter.Frame(card_frame, background='SpringGreen3')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='SpringGreen3', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='SpringGreen3', fg='white').grid(row=3, column=0)

# Embedded frame to hold the player card images
player_card_frame = tkinter.Frame(card_frame, background='SpringGreen3')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# Frame for the Buttons

dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row= 0, column=1)

# Loading cards
cards = []
load_images(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# Create the list to store the dealer's hand and the player's hand
dealer_hand = []
player_hand = []


mainWindow.mainloop()