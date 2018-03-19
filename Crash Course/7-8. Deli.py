sandwich_orders = ['bread', 'lettuce', 'tomato',
                   'cheese', 'olives', 'dressing', 'onions', 'oregano']
finished_sandwiches = []

print('Making your sandwich:')
for _ in range(len(sandwich_orders)):
    s = sandwich_orders.pop()
    print(f'Preparing the {s}.')
    finished_sandwiches.append(s)
print(
    f"Here's your sandwich with"
    f" {', '.join(finished_sandwiches[:-1])} and {finished_sandwiches[-1]}.")
