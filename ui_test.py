# import urwid

# choices = ["Kanye West", "Aphex Twin", "The Beatles", "The Doors", "Fishmans","Kanye West", "Aphex Twin", "The Beatles", "The Doors", "Fishmans","Kanye West", "Aphex Twin", "The Beatles", "The Doors", "Fishmans","Kanye West", "Aphex Twin", "The Beatles", "The Doors", "Fishmans","Kanye West", "Aphex Twin", "The Beatles", "The Doors", "Fishmans"]

# def menu(title, choices):
#     body = [urwid.Text(title), urwid.Divider()]
#     for c in choices:
#         button = urwid.Button(c)
#         urwid.connect_signal(button, 'click', item_chosen, c)
#         body.append(urwid.AttrMap(button, None, focus_map='reversed'))
#     return urwid.ListBox(urwid.SimpleFocusListWalker(body))

# def item_chosen(button, choice):
#     response = urwid.Text([u'You chose ', choice, u'\n'])
#     done = urwid.Button(u'Ok')
#     urwid.connect_signal(done, 'click', menu, 'Pythons', choices)
#     main.original_widget = urwid.Filler(urwid.Pile([response,
#         urwid.AttrMap(done, None, focus_map='reversed')]))
# def exit_program(button):
#     raise urwid.ExitMainLoop()

# main = urwid.Padding(menu(u'Pythons', choices), left=2, right=2)
# top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
#     align='center', width=('relative', 60),
#     valign='middle', height=('relative', 60),
#     min_width=20, min_height=9)
# urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()


# import urwid

# def exit_on_q(key):
#     if key in ('q', 'Q'):
#         raise urwid.ExitMainLoop()

# class QuestionBox(urwid.Filler):
#     def keypress(self, size, key):
#         if key != 'enter':
#             return super().keypress(size, key)
#         self.original_widget = urwid.Text(
#             u"Nice to meet you,\n%s.\n\nPress Q to exit." %
#             edit.edit_text, align='center')

# edit = urwid.Edit(u"What is your name?\n", align='center')
# fill = QuestionBox(edit)
# loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
# loop.run()

# import urwid

# palette = [('I say', 'default,bold', 'default', 'bold'),]
# ask = urwid.Edit(('I say', u"What is your name?\n"))
# reply = urwid.Text(u"")
# button = urwid.Button(u'Exit')
# div = urwid.Divider()
# pile = urwid.Pile([ask, div, reply, div, button])
# top = urwid.Filler(pile, valign='top')

# def on_ask_change(edit, new_edit_text):
#     reply.set_text(('I say', u"Nice to meet you, %s" % new_edit_text))

# def on_exit_clicked(button):
#     raise urwid.ExitMainLoop()

# urwid.connect_signal(ask, 'change', on_ask_change)
# urwid.connect_signal(button, 'click', on_exit_clicked)

# urwid.MainLoop(top).run()


# import urwid

# def question():
#     return urwid.Pile([urwid.Edit(('I say', u"What is your name?\n"))])

# def answer(name):
#     return urwid.Text(('I say', u"Nice to meet you, " + name + "\n"))

# class ConversationListBox(urwid.ListBox):
#     def __init__(self):
#         body = urwid.SimpleFocusListWalker([question()])
#         super(ConversationListBox, self).__init__(body)

#     def keypress(self, size, key):
#         key = super(ConversationListBox, self).keypress(size, key)
#         if key != 'enter':
#             return key
#         name = self.focus[0].edit_text
#         if not name:
#             raise urwid.ExitMainLoop()
#         # replace or add response
#         self.focus.contents[1:] = [(answer(name), self.focus.options())]
#         pos = self.focus_position
#         # add a new question
#         self.body.insert(pos + 1, question())
#         self.focus_position = pos + 1

# palette = [('I say', 'default,bold', 'default'),]
# urwid.MainLoop(ConversationListBox(), palette).run()

import urwid
import time


palette = [('artist','black','light gray')]

Albums_Box = urwid.ListBox(urwid.SimpleFocusListWalker([urwid.Divider()]))

def change_albums(button):
    albums = ["changed"]
    albums_body = [urwid.Divider()]
    for a in albums:
        button = urwid.Button(a)
        albums_body.append(urwid.AttrMap(button, None, focus_map='reversed')) 
    Albums_Box = urwid.ListBox(urwid.SimpleFocusListWalker(albums_body))


choices = ["KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3", "KANYE WEST", "KANYE WEST 2", "KANYE WEST 3"]
artist_body = [urwid.Divider()]
for c in choices:
    button = urwid.Button(c)
    artist_body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    urwid.connect_signal(button, 'click', change_albums)
Artist_Box = urwid.ListBox(urwid.SimpleFocusListWalker(artist_body))







# albums = ["MBDTF", "YANDHI", "YEEZUS"]
# albums_body = [urwid.Divider()]
# for a in albums:
#     button = urwid.Button(a)
#     albums_body.append(urwid.AttrMap(button, None, focus_map='reversed'))
# Albums_Box = urwid.ListBox(urwid.SimpleFocusListWalker(albums_body))

music_player_columns = urwid.Columns([Artist_Box, Albums_Box], dividechars=5)

music_player = urwid.Padding(music_player_columns)



currently_playing = urwid.Text("Currently playing:")
volume = urwid.Text("Volume: 69%", align='right')
footer_columns = urwid.Columns([currently_playing, volume],dividechars=5)
footer = urwid.Filler(footer_columns)

artist_header = urwid.Text("Artists")
album_track_header = urwid.Text("Albums/Tracks", align='right')
header_columns = urwid.Columns([artist_header, album_track_header],dividechars=5)



main_frame = urwid.Frame(music_player, header=header_columns,footer=footer_columns)



urwid.MainLoop(main_frame, palette = [('reversed', 'standout', '')]).run()


while(True):
    print("Album focus: " + Albums_Box.get_focus().get_label())
    print("Artist focus: " + Artist_Box.get_focus().get_label())
    time.sleep(0.5)


# import urwid

# choices = u'Chapman Cleese Gilliam Idle Jones Palin'.split()

# def menu(title, choices):
#     body = [urwid.Text(title), urwid.Divider()]
#     for c in choices:
#         button = urwid.Button(c)
#         urwid.connect_signal(button, 'click', item_chosen, c)
#         body.append(urwid.AttrMap(button, None, focus_map='reversed'))
#     return urwid.ListBox(urwid.SimpleFocusListWalker(body))

# def item_chosen(button, choice):
#     response = urwid.Text([u'You chose ', choice, u'\n'])
#     done = urwid.Button(u'Ok')
#     urwid.connect_signal(done, 'click', exit_program)
#     main.original_widget = urwid.Filler(urwid.Pile([response,
#         urwid.AttrMap(done, None, focus_map='reversed')]))

# def exit_program(button):
#     raise urwid.ExitMainLoop()

# main = urwid.Padding(menu(u'Pythons', choices), left=2, right=2)
# top = urwid.Filler(main) #urwid.SolidFill(u'\N{MEDIUM SHADE}'),
# #     align='center', width=('relative', 60),
# #     valign='middle', height=('relative', 60),
# #     min_width=20, min_height=9)
# urwid.MainLoop(main, palette=[('reversed', 'standout', '')]).run()


