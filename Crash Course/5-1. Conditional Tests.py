foods = ('zucchini', 'tomatoes', 'broccoli', 'corn', 'beans')

beverages = ('water', 'milk', 'coffee', 'tea', 'beer')

for f in foods:
    print(f'{f.title()} is in foods - {f in foods}')

for b in beverages:
    print(f'{b.title()} is in foods - {b in foods}')
