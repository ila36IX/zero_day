#!/bin/python3
from pytube import YouTube, Playlist, Search
from uuid import uuid4
from random import choice
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


def download_mp3(link):
    print(link)
    t = YouTube(link)
    qulities = list(t.streams.filter(only_audio=True))
    fn_first = lambda a: -int(a.abr.split("kbps")[0])
    best_qlt = sorted(qulities, key=fn_first)[0]
    path = str(uuid4().int & (1<<64) -1) + ".webm"
    return best_qlt.download(skip_existing=True, output_path="files")

def random_meme():
    p = Playlist('https://www.youtube.com/playlist?list=PLDxqzeb1l0CHnLsLEWB51upgVrblM6JiF')
    random_link = choice(p)
    return str(random_link)


def yt_search(*queries):
    queries = [q for q in queries if q]
    query = " ".join(queries)
    s = Search(query)
    return s.results[0]


def is_youtube_link(link):
    try:
        t = YouTube(link) 
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    download_mp3("https://youtu.be/8bomsfOD9W4?si=BALoq8hzIRWQpN5y")
