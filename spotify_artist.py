from typing import List


class SpotifyArtist:

   


    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.albums_or_tracks = []

    def __str__(self):
        return self.name   
    
    def get_ID(self):
        return self.id

    def add_album_or_track(self, spotify_abstract):
        self.albums_or_tracks.append(spotify_abstract)

    def get_all(self):
        return self.albums_or_tracks
    