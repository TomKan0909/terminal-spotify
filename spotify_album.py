from typing import List
from spotify_track import SpotifyTrack

class SpotifyAlbum:

    _name: str
    _ID: str
    tracks: List[SpotifyTrack]


    def __init__(self, name, ID):
        self._name = name
        self._ID = ID
        self.tracks = []

    def __str__(self):
        return "Album {} has id: {}".format(self._name, self._ID)    
    
    def get_name(self):
        return self._name
    
    def get_ID(self):
        return self._ID

    def add_tracks(self, spotify_album: SpotifyTrack):
        self.tracks.append(spotify_album)