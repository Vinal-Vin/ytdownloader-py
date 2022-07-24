from importlib.resources import path
from tkinter.filedialog import Open
from pytube import YouTube
from sys import argv
import os

f = open('ytlist.txt', 'r')
outputFolder = "<ADD YOUR OUTPUT PATH>"

youtube_list = f.readlines()

for link in youtube_list:
    yt = YouTube(link)
    yd =  yt.streams.get_highest_resolution()
    print("Downloading: ", yt.title)
    yd.download(outputFolder)
    print("Done")
