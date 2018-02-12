import random
import tkinter

mainWindow = tkinter.Tk()

# Setup of the screen and the frames for the dealer and the player
mainWindow.title('Blackjack')
mainWindow.geometry('1024x768')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=1)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='SpringGreen3')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='SpringGreen3', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='SpringGreen3', fg='white').grid(row=1, column=0)

# Frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background='SpringGreen3')
dealer_card_frame.grid(row=0, column=2, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='SpringGreen3', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='SpringGreen3', fg='white').grid(row=3, column=0)

mainWindow.mainloop()