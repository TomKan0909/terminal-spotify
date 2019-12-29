import os
import sys 
import json 
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotify_album import SpotifyAlbum
from spotify_artist import SpotifyArtist

"""TODO: 1. Extract user's saved albums info q

"""

#Get username from terminal




"""
returns user albums in a dict with artist_id as keys and 
album_ids as values
"""
def current_user_albums_artist(sp):
    #Get first 50 albums
    results = sp.current_user_saved_albums(limit=50,offset=0)
    albums = _current_user_album_artist_helper(results)
    i = 0 
    while results['items'] != []:
        i += 50
        results = sp.current_user_saved_albums(limit=50,offset=i)
        albums.update(_current_user_album_artist_helper(results))
    # return sp.current_user_saved_albums(50) # 50 is max. albums return at once
    return albums

def _current_user_album_artist_helper(results):
    albums = {}
    for item in results['items']:
        album_id = item['album']['id']
        album_artist_id = item['album']['artists'][0]['id']
        if album_artist_id not in albums:
            albums[album_artist_id] = [album_id]
        else:
            albums[album_artist_id].append(album_id)
    return albums
        

def main():
    USER_ID = '31ytkldamhg43ewe6yaspk3lzhvu' 
    play_token = None
    try:
        play_token = util.prompt_for_user_token(USER_ID, 'user-library-read')
    except(AttributeError):
        os.remove(f".cache-{USER_ID}") 
        play_token = util.prompt_for_user_token(USER_ID, 'user-library-read')



    sp = spotipy.Spotify(auth=play_token)
    # sp.start_playback();
    
    print(sp.current_user()["display_name"])
    print(current_user_albums_artist(sp))

        



if __name__ == "__main__":
    main()
