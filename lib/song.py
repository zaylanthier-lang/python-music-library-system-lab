class Song:
    # Class attributes shared by all Song objects
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes for each song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level information when a new song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increase total song count by 1
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add genre only if it is not already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add artist only if they are not already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Count how many songs exist for each genre
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artists_count(cls, artist):
        # Count how many songs exist for each artist
        if artist not in cls.artists_count:
            cls.artists_count[artist] = 1
        else:
            cls.artists_count[artist] += 1