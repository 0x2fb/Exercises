album = {
    'name': 'Modal Soul',
    'artist': 'Nujabes',
    'year': '2005',
    'tracks': [(1, 'Feather'), (2, 'Ordinary Joe'),
               (3, 'Reflection Eternal'), (4, 'Luv'),
               (5, 'Music is mine'), (6, 'Eclipse'),
               (7, 'The Sign'), (8, 'Thank You'),
               (9, "World's End Rhapsody"), (10, 'Modal Soul'),
               (11, 'Flowers'), (12, 'Sea of Cloud'),
               (13, 'Light on the Land'), (14, 'Horizon')]
}

track_titles = list(map(lambda x: x[1], album['tracks']))
print(track_titles)
for x in album['tracks']:
    print(x[1])

tracks = [x[1] for x in album['tracks']]
print(tracks)
