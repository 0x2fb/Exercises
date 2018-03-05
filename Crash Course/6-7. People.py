person1 = {
    'first_name': 'Helen',
    'last_name': 'Jones',
    'age': '34',
    'city': 'Vancouver'
}

person2 = {
    'first_name': 'Steve',
    'last_name': 'Sunderland',
    'age': '42',
    'city': 'Boston'
}

person3 = {
    'first_name': 'Theresa',
    'last_name': 'Hamilton',
    'age': '24',
    'city': 'Seattle'
}

people = [person1, person2, person3]

for person in people:
    for k, v in person.items():
        print(f'{k.title()} - {v.title()}')
