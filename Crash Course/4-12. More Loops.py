my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
friend_foods = my_foods[:]
friend_foods.extend(['olives'])

print('My favorite types of food are:')
for p in my_foods:
    print(f'\t- {p.title()}')

print('Helen\'s favorite types of food are:')
for p in friend_foods:
    print(f'\t- {p.title()}')
