from typing import List
from spotify_abstract import SpotifyAbstract

class SpotifyArtist(SpotifyAbstract):

   


    def __init__(self, name, id):
        super().__init__(name, id)
        self.albums = []

    def __str__(self):
        return self.name   

    def add_album(self, spotify_abstract):
        self.albums.append(spotify_abstract)

    def get_all(self):
        return self.albums