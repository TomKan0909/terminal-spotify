

class SpotifyAbstract:

    """
    Abstract class to represent an album or track
    """

    def __init__(self, name, duration, id):
        self.name = name
        self.duration = duration
        self.id = id    

    # Abstract method
    def __str__(self):
        pass 

    def get_id(self):
        return id
    
    def get_duration(self):
        return duration
    
    

