# Song Class Lab

This project builds a `Song` class that tracks information about songs.

## Features

- Creates song objects with a name, artist, and genre.
- Tracks the total number of songs created.
- Stores a list of unique artists.
- Stores a list of unique genres.
- Tracks how many songs belong to each genre.
- Tracks how many songs each artist has created.

## Example

```python
song1 = Song("Crazy in Love", "Beyonce", "Pop")
song2 = Song("Halo", "Beyonce", "Pop")

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artists_count)