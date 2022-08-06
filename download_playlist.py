from pytube import Playlist
import os


PLAYLIST_LINK = "https://www.youtube.com/playlist?list=PL2788304DC59DBEB4"
SUBDIR_TO_SAVE = "/audio"

pl = Playlist(PLAYLIST_LINK)
for video in pl.videos:
    video.streams.get_audio_only().download(os.getcwd() + SUBDIR_TO_SAVE)