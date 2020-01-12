from typing import List
from spotify_abstract import SpotifyAbstract

""""
Represents a spotify album   
"""
class SpotifyTrack(SpotifyAbstract):

    


    def __init__(self, name, duration, id, track_number):
        self.track_number = track_number
        super().__init__(self, name. duration, id)
        
        

    def __str__(self):
        return self.track_number + ". " + self.name
    

    