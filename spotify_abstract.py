

class SpotifyAbstract:

    """
    Abstract class to represent an album or track
    """

    def __init__(self, name, id):
        self.name = name
        self.id = id    

    # Abstract method
    def __str__(self):
        pass 

    def get_id(self):
        return self.id
    
    
    

