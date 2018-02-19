import random

symbols = ['rock', 'paper', 'scissors']
player = ''
while True:
    computer = random.choice(symbols)
    player_input = input("\n1 - Rock\n2 - Paper\n3 - Scissors\nPick one "
                         "and see if you can beat the computer!\n"
                         "(Press 'q' to quit the program.)").lower()
    if len(player_input) < 1:
        print("Oops, you made a mistake in your entry.")
        continue
    else:
        if player_input == '1' or player_input[0] == 'r':
            player = 'rock'
        elif player_input == '2' or player_input[0] == 'p':
            player = 'paper'
        elif player_input == '3' or player_input[0] == 's':
            player = 'scissors'
        elif player_input == 'q':
            break
        else:
            print("Oops, you made a mistake in your entry.")
            continue
    if computer == player:
        print(f'Draw! The computer also picked {computer.title()}.')
    elif player == 'rock':
        if computer == 'paper':
            print(f'Computer picked {computer.title()} and wins!')
        elif computer == 'scissors':
            print(
                f'Computer picked {computer.title()}, so you win!'
                'Congratulations!')
    elif player == 'paper':
        if computer == 'scissor':
            print(f'Computer picked {computer.title()} and wins!')
        elif computer == 'rock':
            print(
                f'Computer picked {computer.title()}, so you win!'
                ' Congratulations!')
    elif player == 'scissors':
        if computer == 'rock':
            print(f'Computer picked {computer.title()} and wins!')
        elif computer == 'paper':
            print(
                f'Computer picked {computer.title()}, so you win!'
                ' Congratulations!')
    print()
print('Thanks for playing!')
