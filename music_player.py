from spotify_album import SpotifyAlbum
from spotify_track import SpotifyTrack

class SpotifyMusicPlayer:
    
    """"
    :param sp_read: spotify object responsible for read ops
    :type sp_read: spotify object with 'user-library-read' permission

    :param sp_play: spotify object responsible for play ops
    :type sp_play: spotify object with 'user-modify-playback' permission

    :param sp_currently_playing: spotify object responsible for 
    retrival of currently playing track info
    :type sp_currently_playing: spotify object with 
    'user-read-currently-playing' permission
    
    :param sp_artists: List of artists that the user has albums for
    :type sp_artists: List[SpotifyArtist]
    """

    def __init__(self, sp_read, sp_play, sp_currently_playing, sp_artists):
        self.sp_read = sp_read
        self.sp_play = sp_play
        self.sp_currently_playing = sp_currently_playing
        self.sp_artists = sp_artists
        self.currently_playing = None
        self.volume = 100
        self.sp_play.volume(100)

    def playback(self, sp_album_track):
        sp_album_track_id = sp_album_track.get_id()
        context_uri = None
        if isinstance(sp_album_track, SpotifyAlbum):
            context_uri = self.sp_read.album(sp_album_track_id)["uri"]
        elif isinstance(sp_album_track, SpotifyTrack):
            context_uri = self.sp_read.track(sp_album_track_id)["uri"] 
        
        self.sp_play.start_playback(context_uri=context_uri)
        self.currently_playing = sp_currently_playing.current_user_playing_track()['item']['name']

    def get_currently_playing(self):
        self.currently_playing = sp_currently_playing.current_user_playing_track()['item']['name']
        return self.currently_playing


    def increase_volume(self):
        if self.volume >= 100:
            return
        else
            self.volume += 5
            self.sp_play.volume(self.volume)
    
    def decrease_volume(self):
        if self.volume <= 0:
            return
        else
            self.volume -= 5
            self.sp_play.volume(self.volume)
    
    def get_volume(self):
        return self.volume