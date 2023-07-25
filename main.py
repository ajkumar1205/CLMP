from os import system as CMD
from os import get_terminal_size

from utils import *

# mixer.music.set_endevent()
# THIS mixer.music.set_endevent WILL BE USED FOR AUTO CHANGING TO NEXT SONG

CMD("cls")
width, line = get_terminal_size()
# THIS IS OUR SONG PLAYING SCREEN WHICH WILL TAKE US TO ANOTHER WHILE LOOP
def music_screen(clmp):
    CMD("cls")
    print(" Music Player ".center(44, '='))
    print("Now Playing: ")
    for _ in range(44):
        print("-", end="")
    print("\n")
    print(clmp.list_pointer[clmp.current_index].absolute)
    print("")
    for _ in range(width):
        print("-", end="")
    print("\n")
    print("To See Playlist enter: ".rjust(width+1, ' '))
    print("list".rjust(width, ' '))
    print("ls".rjust(width, ' '))
    print("songs".rjust(width, ' '))
    print("songs_list".rjust(width, ' '))
    print("")
    for _ in range(width):
        print("~", end="")
    print("")
    print("More Options".center(width, ' '))
    print("Change", end='')
    print("index".rjust(38, ' '))
    print("Pause", end='')
    print("pause, pa, ps".rjust(width-5, ' '))
    print("Unpause", end='')
    print("play, p".rjust(width-7, ' '))
    print("Repeat", end='')
    print("repeat, r, re".rjust(width-6, ' '))
    print("Exit", end='')
    print("exit, break, x, e".rjust(width-4, ' '))
    for _ in range(width):
        print("~", end="")
    print("\n")
# HERE I HAVE TO IMPLEMENT ANOTHER WHILE LOOP WHICH WILL DEAL WITH SETTING LIST
    # while True:
    #     cmd = input()
    #     upnext = []
        # cmd_list = cmd.split(' ')
        # elif cmd_list[0] == 'set':
        #     for i in range(len(cmd_list)-2):
        #         try:
        #             upnext.insert(-1, int(cmd_list(i+1)))
        #         except:
        #             pass
        # elif ['shuffle', 's', 'sf'].__contains__(cmd):
        #     print("Shuffle :On")



clmp = CLMP()
print(" Command Line Music player ".center(width, '='))
print("Total number of songs in this directory: ", clmp.songs)
print("Type help or clmp h for help")


while True:
    cmd = input()
    cmd = cmd.lower()
    cmd_list = cmd.split(' ')
    try:
        cmd = int(cmd)
        cmd = cmd%clmp.songs
        clmp.play_song(cmd)
        music_screen(clmp)
    except:
        if ['songs', 'list', 'songs_list', 'ls'].__contains__(cmd):
            CMD("cls")
            clmp.show_songs()

        elif ['pause', 'pu', 'ps', 'pa'].__contains__(cmd):
            print("~~Song Paused~~".center(width, ' '))
            clmp.pause_song()

        elif ['play', 'p'].__contains__(cmd):
            clmp.unpause_song()
        
        elif ['r', 're', 'repeat'].__contains__(cmd):
            clmp.repeat()

        elif ['help', 'clmp h'].__contains__(cmd):
            # YOU HAVE TO SETUP THE HELP HERE AFTER WRITING ALL THE COMMANDS IN ALL SCREENS
            print("Help will be here")

        elif cmd_list[0] == 'set':
            # for i in range(1,len(cmd_list)-1):
                pass
                # try:
                #     upnext.insert(-1, int(cmd_list(i)))
                # except:
                #     pass
        elif ['shuffle', 's', 'sf'].__contains__(cmd):
            clmp.shuffle = True
            clmp.shuffle_list()

        elif ['exit', 'break', 'x', 'e'].__contains__(cmd):
            CMD("cls")
            clmp.close()
            break
        else:
            print("Type help or clmp h for help")
