def make_album(artist_name, album_title, tracks=None):
    album_dict = {}
    album_dict[artist_name] = album_title
    if tracks:
        album_dict[artist_name] = (album_title, tracks)
    return album_dict


print(make_album('Arcade Fire', 'The Suburbs'))
print(make_album('Pixies', 'Surfer Rosa', 5))
print(make_album('Beck', 'Sea Change'))
