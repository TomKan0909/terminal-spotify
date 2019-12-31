import os
import sys 
import json 
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotify_album import SpotifyAlbum
from spotify_artist import SpotifyArtist






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

"""helper method for current_user_albums_artists"""
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
    read_token = None
    try:
        read_token = util.prompt_for_user_token(USER_ID, 'user-library-read')
        play_token = util.prompt_for_user_token(USER_ID, 'user-modify-playback-state')
    except(AttributeError):
        os.remove(f".cache-{USER_ID}") 
        read_token = util.prompt_for_user_token(USER_ID, 'user-library-read')
        play_token = util.prompt_for_user_token(USER_ID, 'user-modify-playback-state')



    sp_read = spotipy.Spotify(auth=read_token)
    sp_play = spotipy.Spotify(auth=play_token)
    # sp_play.start_playback(context_uri='spotify:album:1vWnB0hYmluskQuzxwo25a')
    
    #Get artists albums dictionary
    usr_albums = current_user_albums_artist(sp_read)
    #Get artist_id
    artists = list(usr_albums.keys())
    #Lambda function to turn artist id into strings
    artist_name = lambda artist_id: (sp_read.artist(artist_id))["name"]
    artists_name = [artist_name(artist) for artist in artists]
    artists_name_list = list(enumerate(artists_name, 1))

    for item in artists_name_list:
        print(item)

    usr_input = int(input("pick an artist by entering number between 1 and {}: "  
                    .format(len(artists_name_list))))
    
    if usr_input < 1 or usr_input > len(artists_name_list):
        usr_input = input("pick an artist by entering number between 1 and {}: "
                        .format(len(artists_name_list))) 
    else:
        picked_artist = artists[usr_input - 1]
        picked_artists_context_uri = sp_read.artist(picked_artist)["uri"]
        sp_play.start_playback(context_uri=picked_artists_context_uri)
        print("Currently playing {}".format(artist_name(picked_artist)))


    



        



if __name__ == "__main__":
    main()
