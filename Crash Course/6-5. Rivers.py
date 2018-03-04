rivers = {
    'nile': 'egypt',
    'danube': 'germany',
    'seine': 'france'
}
print()
for k, v in rivers.items():
    print(f'The river {k.title()} runs through {v.title()}.\n')
print('Rivers:\n\t')
for r in rivers:
    print(r.title(), end='\t')
print('\n\nCountries:\n\t')
for c in rivers.keys():
    print(c.title(), end='\t')
print('\n')
