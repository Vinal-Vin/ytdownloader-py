from importlib.resources import path
from tkinter.filedialog import Open
from pytube import YouTube

f = open('ytlist.txt', 'r')
outputFolder = "<ADD YOUR OUTPUT PATH>"

youtube_link_lists = f.readlines()

for link in youtube_link_lists:
    yt = YouTube(link)
    yd =  yt.streams.get_highest_resolution()
    print("Downloading: ", yt.title)
    yd.download(outputFolder)
    print("Done")
