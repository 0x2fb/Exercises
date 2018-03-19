age = input('Plase enter your age: ')
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('Your ticket is free.')
    elif 3 <= age < 12:
        print('Your ticket costs $10.')
    elif 12 <= age:
        print('Your ticket costs $15.')
    age = input('Plase enter your age: ')
