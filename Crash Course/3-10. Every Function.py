games = ['Don\'t Starve', 'Factorio', 'Hacknet']
games.append('Darkest Dungeon')
games.append('Fallout 4')
del games[4]
favorite = games.pop(2)
games.insert(0, favorite)
games.insert(1, 'Sleeping Dogs')
awesome = 'Sleeping Dogs'
games.remove(awesome)
games.append(awesome)
print(games)
print(sorted(games))
games.sort()
print(games)
games.reverse()
print(games)
print(f'There are {len(games)} games in the list.')