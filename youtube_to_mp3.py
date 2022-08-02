from pytube import Playlist
import os


link = "https://www.youtube.com/playlist?list=PL2788304DC59DBEB4"
pl = Playlist(link)
for video in pl.videos:
    video.streams.get_audio_only().download(os.getcwd() + "/audio")
    print(f"{video.title} downloaded.")