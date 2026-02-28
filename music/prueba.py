# pip install yt-dlp - librería
import yt_dlp as yt 

url = input("Enter YouTube Video Link: ") # Se ingresa el Link de Youtube y se almacena en "url"

yt_opts = {'format' : 'best'} # Descarga en la mejor resolución

with yt.YoutubeDL(yt_opts) as ydl:
    ydl.download([url])
    
print("Descarga completada!")





