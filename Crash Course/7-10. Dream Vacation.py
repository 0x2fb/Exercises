destinations = []

user_input = input('Where would you like to travel to?')
while True:
    if user_input == 'quit':
        break
    else:
        destinations.append(user_input)
        user_input = input('Where would you like to travel to?')
print(
    f'You would like to go to {", ".join(destinations[:-1])}'
    f' and {destinations[-1]}')
