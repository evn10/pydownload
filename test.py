#!/home/ake/.venv/bin/python3

from pytubefix import YouTube

url = input("url >")

#yt = YouTube(url, use_po_token=True)
yt = YouTube(url, "WEB")
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()
