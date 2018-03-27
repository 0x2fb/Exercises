album_dict = {}


def make_album(artist_name, album_title, tracks=None):
    if tracks:
        album_dict[artist_name] = (album_title, tracks)
    else:
        album_dict[artist_name] = (album_title,)


while True:
    artist_name = input('Please enter the name of the artist: \n')
    if artist_name == 'q':
        break
    album_title = input('Please enter the name of the album: \n')
    if album_title == 'q':
        break
    tracks = input('Please enter the number of tracks if you know it: \n')
    if tracks == 'q':
        break
    make_album(artist_name, album_title, tracks)
print(album_dict)
