from __future__ import unicode_literals
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

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],

}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])


