pizza_toppings = []
while True:
    topping = input('Please name a topping that you would like to add.'
                    'Type "quit" when you are done.')
    if topping == "quit":
        break
    else:
        pizza_toppings.append(topping)
        print(f'{topping.title()} added to your pizza.')

print('Your pizza consists of:')
for p in pizza_toppings:
    print(f'\t{p.title()}')
