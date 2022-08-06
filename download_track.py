from pytube import YouTube
import os


TRACK_LINK = "https://www.youtube.com/playlist?list=PL2788304DC59DBEB4"
SUBDIR_TO_SAVE = "/audio"

video = YouTube(TRACK_LINK)
video.streams.get_audio_only().download(os.getcwd() + SUBDIR_TO_SAVE)