from pygame import mixer
from os import get_terminal_size
from pathlib import Path
from threading import Thread

import pygame
import random

pygame.init()
width, lines = get_terminal_size()

MP3 = 'mp3'
MEMORY = ["D:\\"]

END = pygame.USEREVENT + 1
SONGEND = pygame.event.Event(END)
pygame.event.post(SONGEND)

class CLMP:
    def __init__(self):
        mixer.init()
        self.place = Path.cwd()
        self.songs_list = []
        self.upnext_playlist = []
        self.list_pointer = self.songs_list
        self.shuffle = False
        self.current_index = -1
        self.songs = 0
        mixer.music.set_endevent(END)
        self.fetch_all_songs()
        # Thread(target=self.fetch_all_songs, args=()).start()

    def fetch_all_songs(self):
        for path in MEMORY:
            self.fetch_songs(path)
        # Thread(target=self.endSong, args=()).start()

    def fetch_songs(self, path):
        dir_list = []
        try:
            for file in Path(path).iterdir():
                if file.is_dir():
                    dir_list.append(file)
                elif file.is_file():
                    if str(file)[-3:] == 'mp3':
                        self.songs_list.insert(-1, file)
                        self.upnext_playlist.insert(-1, file)
            while len(dir_list) > 0:
                f = dir_list.pop()
                self.fetch_songs(path)
        except:
            pass

    def play_song(self, index):
        self.current_index = index-1
        try:
            mixer.music.stop()
            mixer.music.unload()
        except:
            pass
        mixer.music.load(self.list_pointer[self.current_index])
        mixer.music.play() 
        mixer.music.queue(self.list_pointer[self.current_index+1])

    def pause_song(self):
        mixer.music.pause()

    def unpause_song(self):
        mixer.music.unpause()

    def repeat(self):
        mixer.music.rewind()

    def show_songs(self):
        print(" Command Line Music player ".center(width, '='))
        for x in range(len(self.songs_list)):
            print(x.absolute)

    def close(self):
        mixer.music.pause()
        mixer.music.unload()

    def next(self):
        mixer.music.stop()
        mixer.music.unload()

    def prev(self):
        mixer.music.stop()
        mixer.music.unload()
        

    def shuffle_list(self):
        random.shuffle(self.upnext_playlist)

    def endSong(self):
        while True:
            for event in pygame.event.get():
                if event == SONGEND:
                    index = (self.current_index + 1)%self.songs
                    mixer.music.queue(self.list_pointer[index])

