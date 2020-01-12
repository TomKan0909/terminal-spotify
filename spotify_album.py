from typing import List
from spotify_abstract import SpotifyAbstract


""""
Represents a spotify album   
"""
class SpotifyAlbum(SpotifyAbstract):

    


    def __init__(self, name, duration, id):
        super().__init__(self, name. duration, id)
        

    def __str__(self):
        return self.name + " (Album)"  
    
