class Artist:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_song(self, album_name, year, song_title):
        current_album = find_object(album_name, self.albums)
        if current_album is None:
            current_album = Album(album_name, year, self.name)
            self.albums.append(current_album)
        current_album.add_song(song_title)


class Album:

    def __init__(self, name, year, artist):
        self.name = name
        self.year = year
        self.artist = artist
        self.tracks = []

    def add_song(self, song_title):
        current_song = find_object(song_title, self.tracks)
        if current_song is None:
            current_song = Song(song_title, self.artist)
            self.tracks.append(current_song)


class Song:

    def __init__(self, title, artist):
        self.name = title
        self.artist = artist


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():

    artist_list = []

    with open('albums.txt', 'r') as textfile:
        for line in textfile:
            artist_field, album_field, year_field, song_field = tuple(
                line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f"{artist_field}:{album_field}:{year_field}:{song_field}")

            current_artist = find_object(artist_field, artist_list)
            if current_artist is None:
                current_artist = Artist(artist_field)
                artist_list.append(current_artist)

            current_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for current_artist in artist_list:
            for current_album in current_artist.albums:
                for current_song in current_album.tracks:
                    print(f"{current_artist.name}\t{current_album.name}\t"
                          f"{current_album.year}\t{current_song.name}",
                          file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print(f"There are {len(artists)} artists")
    create_checkfile(artists)
