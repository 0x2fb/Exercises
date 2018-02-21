threes = list(range(3, 31, 3))

print('The first three items in the list are:')
for i in threes[0:3]:
    print(i)

print('Three items in the middle of the list are:')
for i in threes[int((len(threes) / 2) - 3):int((len(threes) / 2))]:
    print(i)

print('The last three items in the list are:')
for i in threes[:-4:-1]:
    print(i)
