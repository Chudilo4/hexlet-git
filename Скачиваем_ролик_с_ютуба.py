# coding: utf-8

import pytube
from pytube.cli import on_progress

url=input('URL :')
yt = pytube.YouTube(url,on_progress_callback=on_progress)
stream=yt.streams
stream1=''
for s in str(stream):
    if s!=',':
        stream1+=s
    else:
        stream1+='\n'
print(stream1)
itag=input('Введите нужный вам номер itag : ')
video = stream.get_by_itag(itag)

video.download()
print("(:")
