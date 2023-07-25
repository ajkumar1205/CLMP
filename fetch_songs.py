import pathlib as pl
# import time


audio_list1 = []
songs_name = []
audio_list2 = []

path = pl.Path("D:\\")

def fetch1(path):
    for file in pl.Path(path).iterdir():
        try:
            if file.is_dir():
                # print(file)
                fetch1(file)
            elif file.is_file():
                if str(file)[-3:] == 'mp3':
                    audio_list1.append(file)
                    # print(file)
        except:
            pass

def fetch2(path):
    dir_list = []
    try:
        for file in pl.Path(path).iterdir():
            if file.is_dir():
                dir_list.append(file)
            elif file.is_file():
                if str(file)[-3:] == 'mp3':
                    audio_list2.append(file)
                    songs_name.append(file.name)
        while len(dir_list) > 0:
            f = dir_list.pop()
            fetch2(f)
    except:
        pass

    
# fetch2(path)

# print(songs_name)

# tic1 = time.time()
# fetch1(path)
# toc1 = time.time()

# tic2 = time.time()
# fetch2(path)
# toc2 = time.time()

# print("Ratio of fetch1 to fetch2: "+str((toc1-tic1)/(toc2-tic2)))