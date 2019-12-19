import os
import sys 
import json 
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

"""TODO: 1. Extract user's saved albums info 

"""

#Get username from terminal



USER_ID = '31ytkldamhg43ewe6yaspk3lzhvu' 

def current_user_albums_artist(sp):
    results = sp.current_user_saved_albums(limit=50,offset=0)
    albums = results
    i = 0 
    while results['items'] != []:
        i += 50
        results = sp.current_user_saved_albums(limit=50,offset=i)
        albums.update(results)
    # return sp.current_user_saved_albums(50) # 50 is max. albums return at once
    return albums


def _cur_usr_alb_help(js, albums):
    for item in js['items']:
        artist = item["album"]["artists"]["name"]
        if artist not in albums:
            albums[artist] = {} # albums of artist; formart (nameOfAlbum : albumURI)
        
    pass



def main():
    try:
        token = util.prompt_for_user_token(USER_ID, 'user-library-read')
    except(AttributeError):
        os.remove(f".cache-{USER_ID}") 
        token = util.prompt_for_user_token(USER_ID, 'user-library-read') 


    sp = spotipy.Spotify(auth=token)

    
    # result = current_user_albums_artist(sp)
    result = json.dumps(sp.current_user_saved_albums(limit=1), sort_keys= True, indent=4)
    # albums = {}
    # for album in result:
        
    # result = current_user_albums(sp)
    f = open('text.txt', 'w')
    for line in result:
        f.write(line)



if __name__ == "__main__":
    main()

# # Get artist image
# artist = input("Enter artist: ")

# results = sp.search(q='artist:' + artist, type='artist')
# items = results['artists']['items']
# if len(items) > 0:
#     artist = items[0]
#     print (artist['name']) 
#     print ('---------------------------------')
#     for i in range(len(artist['images'])):
#         print (artist['images'][i]['url']) # ['url']