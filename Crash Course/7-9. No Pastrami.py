sandwich_orders = ['bread', 'lettuce', 'tomato', 'pastrami',
                   'cheese', 'olives', 'dressing', 'pastrami',
                   'onions', 'oregano', 'pastrami']
finished_sandwiches = []

print('Making your sandwich:')
while sandwich_orders:
    s = sandwich_orders.pop()
    if s == 'pastrami':
        print('Oh no, we have run out of pastrami!')
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
    else:
        print(f'Preparing the {s}.')
        finished_sandwiches.append(s)
print(
    f"Here's your sandwich with"
    f" {', '.join(finished_sandwiches[:-1])} and {finished_sandwiches[-1]}.")
