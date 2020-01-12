import urwid
import typing
import random

class Ui():
    """
    Ui class that uses urwid, should be compatible with any music_player
    abstract class 

    :param _music_player: the music_player that is interface injected into the 
    ui class
    :type _music_player: music_player interface instance
    
    :param artist_body: the column that contains all the artist of the user
    :type artist_body: urwid.ListBox 

    """    

    # Artist name as KEY and spotify artist object as VALUE 
    palette = [('artist','black','light gray')]

    def __init__(self, music_player):
        self.music_player = music_player
        self.artist_name_dict = {}
        self.currently_playing = None
        self.volume = 100
        self.albums_body = []


    # Set up contents of the artist column
    def init_artist_body(self):
        self.artist_body = []
        #Get all artist and store it in list; need to implement
        #temporary for testing
        artists = ["KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3"]
        for artist in artists:
            #implement get_name method for spotify artist
            button = urwid.Button(artist.__str__())
            urwid.connect_signal(button, 'click', self.display_artist_albums_track, 
            artist)
            self.artist_body.append(urwid.AttrMap(button, None, focus_map='reversed'))
            self.artist_name_dict[artist.__str__()] = artist
            
    # Set up contents of the albums/tracjs column
    def display_artist_albums_track(self, button, artist):
        
        #Get all albums/tracks for spotify artist; need to be implemented
        self.albums_body = []
        albums_tracks = [["beef ", "beef "], ["chicken","chicken"]]        
        for at in random.choice(albums_tracks):
            button = urwid.Button(at.__str__())
            urwid.connect_signal(button, 'click', self.playback, at)
            self.albums_body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        
        self.albums_list_walker = urwid.SimpleFocusListWalker(self.albums_body) 

        self.albums_box = urwid.ListBox(self.albums_list_walker)
        

        self.player_ui_columns = urwid.Columns([self.artist_box, self.albums_box], dividechars=5)
        self.player_ui = urwid.Padding(self.player_ui_columns)
        self.player_ui_frame.set_body(self.player_ui)


    # To play a track/album
    def playback(self, button, at):

        #Get album or track id 
        self.music_player.playback(at)
        self.currently_playing = at.__str__()
        self.current_play_text.set_text("Currently playing: {}".format(self.currently_playing))
        
    
    #increase volume
    def increase_volume(self):
        self.music_player.increase_volume()
        self.volume_text.set_text("Volume: {}".format(self.music_player.get_volume()), align='right')

    #decrease volume
    def decrease_volume(self):
        self.music_player.decrease_volume()
        self.volume_text.set_text("Volume: {}".format(self.music_player.get_volume()), align='right')
    

    def update_albums_box(self, _loop, _data):
        

        test = ["1", "2", "3", "4"]

        self.currently_playing_text.set_text("Currently playing: {}".format(self.music_player.get_currently_playing()))

        # self.currently_playing_text = urwid.Text("Currently playing: {}".format(random.choice(test)))
        # self.volume_text = urwid.Text("Volume: {}".format(random.choice(test)), align='right')
        self.footer_columns = urwid.Columns([self.currently_playing_text, self.volume_text],dividechars=5)
        self.footer_pile = urwid.Pile([urwid.Divider(), self.footer_columns])
        self.player_ui_frame.set_footer(self.footer_pile)



        _loop.set_alarm_in(0.1, self.update_albums_box)



    def draw_ui(self):
        
        #Make artist/albums columns
        self.init_artist_body()
        self.artist_list_walker = urwid.SimpleFocusListWalker(self.artist_body)
        self.albums_list_walker = urwid.SimpleFocusListWalker(self.albums_body) 

        self.artist_box = urwid.ListBox(self.artist_list_walker)
        self.albums_box = urwid.ListBox(self.albums_list_walker)
        
        #Footer
        self.currently_playing_text = urwid.Text("Currently playing: {}".format(self.currently_playing))
        self.volume_text = urwid.Text("Volume: {}".format(self.volume), align='right')
        
        self.footer_columns = urwid.Columns([self.currently_playing_text, self.volume_text],dividechars=5)
        self.footer_pile = urwid.Pile([urwid.Divider(), self.footer_columns])

        #Header
        self.artist_header = urwid.Text("Artists")
        self.album_track_header = urwid.Text("Albums/Tracks")
        self.header_columns = urwid.Columns([self.artist_header, self.album_track_header],dividechars=5)
        self.header_pile = urwid.Pile([self.header_columns, urwid.Divider()])

        #Main frame
        self.player_ui_columns = urwid.Columns([self.artist_box, self.albums_box], dividechars=5)
        self.player_ui = urwid.Padding(self.player_ui_columns)
        self.player_ui_frame = urwid.Frame(self.player_ui, header=self.header_pile, footer=self.footer_pile) 

       
        
        



    #TODO: implement methods for key handling
    # def handle_keys(self, key):
    #     if(key=='q'):
    #         raise urwid.ExitMainLoop()

    #     method_dict = {
    #         'v': , #change volume down
    #         'b': , #change volume up
    #         'p': , #play 
    #         'o': ,  #pause
    #     }
    

    #     try:
    #         method_dict[key]() 
    #     except:
    #         pass




if __name__ == '__main__':

    mp = 5
    p = Ui(mp)
    p.draw_ui()
    arg = p.player_ui_frame
    loop = urwid.MainLoop(p.player_ui_frame, palette = [('reversed', 'standout', '')])
    loop.set_alarm_in(2, p.update_albums_box)
    loop.run()