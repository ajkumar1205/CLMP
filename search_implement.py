import re
from fetch_songs import path, fetch2, songs_name

# fetch2(path)

# search_map = {}

# i = 1
# for song in songs_name:
#     search_map[i] = set(re.split("[ -@[-`{-~]", str(song).lower()))
#     i += 1

class SongKeys():
    def __init__(self, keys: set, value: int):
        self.keys = keys
        self.value = value

    def get(self, str : str):
        if str in self.keys:
            return self.value
        else:
            return None
        
    def __str__(self):
        return f"{self.keys} -> {self.value}"
    
    def contains(self, str: str):
        return str in self.keys

song1 = "jo bhi mai kahna chahun barbaad kre alfaaz mere.mp3"
song2 = "akkad bakkad bambe boy assi nabe pure so.mp3"
song3 = "o re piyaa hayee.mp3"

search_set = set()

search_set.add(SongKeys(set(re.split(" ", song1.lower())), 1))
search_set.add(SongKeys(set(re.split(" ", song2.lower())), 2))
search_set.add(SongKeys(set(re.split(" ", song3.lower())), 3))

while True:
    cmd = input()
    if cmd == 'x':
        break
    else:
        for sk in search_set:
            if sk.contains(cmd):
                print(sk.get(cmd))

