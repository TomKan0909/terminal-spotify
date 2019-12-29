class SpotifyTrack:

    _name: str
    _ID: str
    _track_number: int


    def __init__(self, name, ID, track_number):
        self._name = name
        self._ID = ID
        self._track_number = track_number

    def __str__(self):
        return "Track {} has id: {}".format(self._name, self._ID)    
    
    def get_name(self):
        return self._name
    
    def get_ID(self):
        return self._ID

    def get_track_number(self):
        return self._track_number