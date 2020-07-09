import os
import sys 
import json 
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotify_album import SpotifyAlbum
from spotify_artist import SpotifyArtist
from spotify_track import SpotifyTrack
from music_player import SpotifyMusicPlayer
from ui import Ui
import urwid




"""
returns user albums in a dict with artist_id as keys and 
album_ids as values
"""
artist_id_to_artist = {}

def current_user_albums_artist(sp):
    #Get first 50 albums
    results = sp.current_user_saved_albums(limit=50,offset=0)
    _current_user_album_artist_helper(results)
    i = 0 
    while results['items'] != []:
        i += 50
        results = sp.current_user_saved_albums(limit=50,offset=i)
        _current_user_album_artist_helper(results)
        

"""helper method for current_user_albums_artists"""
def _current_user_album_artist_helper(results):
    albums = {}
    for item in results['items']:
        album_id = item['album']['id']
        album_name = item['album']['name']
        album = SpotifyAlbum(album_name, album_id)
               


        album_artist_name = item['album']['artists'][0]['name']
        album_artist_id = item['album']['artists'][0]['id']

        if album_artist_id not in albums:
            albums[album_artist_id] = [album_id]
        else:
            albums[album_artist_id].append(album_id)

        #New stuff
        if album_artist_id not in artist_id_to_artist:
            artist_id_to_artist[album_artist_id] = SpotifyArtist(album_artist_name, album_artist_id)
        
        for track in item['album']['tracks']['items']:
            track_name = track['name']
            track_id = track['id']
            track_number = track['track_number']
            spotify_track = SpotifyTrack(track_name, track_id, track_number)
            album.add_track(spotify_track)

        artist_id_to_artist[album_artist_id].add_album(album)
        




    return artist_id_to_artist
        

def main():
    USER_ID = '31ytkldamhg43ewe6yaspk3lzhvu' 
    play_token = None
    read_token = None
    current_token = None
    try:
        read_token = util.prompt_for_user_token(USER_ID, 'user-library-read')
        play_token = util.prompt_for_user_token(USER_ID, 'user-modify-playback-state')
        current_token = util.prompt_for_user_token(USER_ID, 'user-read-currently-playing')
    except(AttributeError):
        os.remove(f".cache-{USER_ID}") 
        read_token = util.prompt_for_user_token(USER_ID, 'user-library-read')
        play_token = util.prompt_for_user_token(USER_ID, 'user-modify-playback-state')
        current_token = util.prompt_for_user_token(USER_ID, 'user-read-currently-playing')


    sp_read = spotipy.Spotify(auth=read_token)
    sp_play = spotipy.Spotify(auth=play_token)
    sp_current = spotipy.Spotify(auth=current_token)

    
    #Get artists albums dictionary

    current_user_albums_artist(sp_read)
    #Get artist_id
    artists = list(artist_id_to_artist.values())
    artists_readable = [a.__str__() for a in artists]

    mp = SpotifyMusicPlayer(sp_read, sp_play, sp_current, artists)

    p = Ui(mp)
    p.draw_ui()
    loop = urwid.MainLoop(p.player_ui_frame, palette = [('reversed', 'standout', '')], unhandled_input=p.handle_keys)
    loop.set_alarm_in(2, p.update_albums_box)
    loop.run()


    



if __name__ == "__main__":
    main()
