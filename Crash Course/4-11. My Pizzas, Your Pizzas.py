favorite_pizzas = ['mozzarella', 'tomatoes', 'rucola']
friends_pizzas = favorite_pizzas[:]
friends_pizzas.append('olives')

print('My favorite pizzas toppings are:')
for p in favorite_pizzas:
    print(f'\t- {p.title()}')

print('Helen\'s favorite pizzas toppings are:')
for p in friends_pizzas:
    print(f'\t- {p.title()}')
