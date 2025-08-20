class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre and self.genre not in self.genres:
            self.genres.append(self.genre)
        self.add_to_genre_count(self.genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    def add_to_artists(self):
        if self.artist and self.artist not in self.artists:
            self.artists.append(self.artist)
        self.add_to_artist_count(self.artist)

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1