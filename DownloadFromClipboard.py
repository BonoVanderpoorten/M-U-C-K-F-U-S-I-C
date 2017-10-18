import youtube_dl
from pydub import AudioSegment
import pyperclip
import pafy
import os

#ONLY USE THIS ON MUSIC YOU OWN OR THAT ISN'T COPYRIGHTED
#hehe xd

#CONFIG------------------------
#Music folder location
musicfolder = "D:\Music\MUCKFUSIC"
#------------------------------
#Set working folder to Music folder
os.chdir(musicfolder)
#Getting URL out the clipboard
url = pyperclip.paste()
print('URL is: '+url)
#Saving the title for naming later
title = pafy.new(url).title
print('Title is: '+title)
#Downloading the video, it's a videofile but with only audio
video = pafy.new(url).getbestaudio().download()
#Strip the audio from video
sound = AudioSegment.from_file(video)
print("Segmented the audio.")
#Removing the videofile
os.remove(video)
print("Removed videofile.")
#Making of the file name:
filename = title+".mp3"
#Saving the mp3
sound.export(filename, format="mp3")
#Removing the videofile
print("All done.")




