from typing import List
from spotify_abstract import SpotifyAbstract


""""
Represents a spotify album   
"""
class SpotifyAlbum(SpotifyAbstract):

    


    def __init__(self, name, id):
        super().__init__(name, id)
        self.tracks = [] 

    def __str__(self):
        return self.name + " (Album)"  

    def add_track(self, track):
        self.tracks.append(track)    
    
    def get_tracks(self):
        return self.tracks
