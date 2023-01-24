from pytube import YouTube
from pytube import Playlist
import os

url = ""                # link de la lista de youtube, la lista tiene que ser pública
folder = "./"           # Carpeta en la que se van a guardar los mp3


pl = Playlist(str(url))
for i in pl.videos:
    try:
        # extract only audio
        audios = i.streams.filter(only_audio = True).first() 
        
        # download the files
        archivo = audios.download(output_path = folder)
        
        # save the file
        base, ext = os.path.splitext(archivo)
        convertido = base + '.mp3'
        os.rename(archivo, convertido)
        
    except FileExistsError:
        os.remove(base + '.mp4')