from typing import List
from spotify_album import SpotifyAlbum

class SpotifyArtist:

    _name: str
    _ID: str
    albums: List[SpotifyAlbum]


    def __init__(self, name, ID):
        self._name = name
        self._ID = ID
        self.albums = []

    def __str__(self):
        return "Artist {} has id: {}".format(self._name, self._ID)    
    
    def get_name(self):
        return self._name
    
    def get_ID(self):
        return self._ID

    def add_album(self, spotify_album: SpotifyAlbum):
        self.albums.append(spotify_album)

    def get_all_albums(self):
        return self.albums
    