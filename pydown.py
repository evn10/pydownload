#!/home/ake/.venv/bin/python3

from typing import Callable, Optional
from pytubefix import YouTube
from pytubefix.cli import on_progress
import requests
import json

class PyDown:
    def __init__(self, po_token):
            self.use_po_token = True if po_token == True else False
            use_oauth: bool = False,
            allow_oauth_cache: bool = True,
            token_file: Optional[str] = "Mlsjwi2eNGYlESP6as1RxdBtuiOeVx2TQXRYkQXTyLxzJHL82WTvJcs7IHq28dw8u3_aIavemIMDh-VZKGjACCC1ScY4F6R9DNUQEC1oLbp5UmUSjMDkgGSd2s3E"
            outh_verifier: Callable[[str, str], None]|None="CgtXa0l5Q2N4enQxUSjN0ci_BjInCgJCRRIhEh0SGwsMDg8QERITFBUWFxgZGhscHR4fICEiIyQlJiAv"

    def sanitize_filename(self, filename):
        return "".join(c if c.isalnum() or c in " ._-" else "_" for c in filename)

    def Download(self,url,audio_only : True) -> int:
        try:
            yt = YouTube(url, on_progress_callback = on_progress)
            print(yt.title)
            yt_title = self.sanitize_filename(yt.title)
            if audio_only:
               ys = yt.streams.get_audio_only()
               ys.download(output_path="/home/ake/Downloads/", filename=f'{yt_title}.mp3')
            else:
               ys.streams.get_highest_resolution()
               ys.download(output_path="/home/ake/Downloads")
              
        except Exception as err:
            print(f"An error {err=} has occurred with type {type(err)=}")
            raise
            return -1
        return 0 # all went well

py = PyDown(True)

url = input("Enter the YouTube video URL: ")
audio_only = input("Audio Only <Y>: ") or True

headers = {'user-agent': 'customize header string', 'Content-Type': 'application/json; charset=utf-8'}  

r = requests.get(url)
r.raise_for_status()

rc = py.Download(url, True)
if (rc == 0) : 
    print("\rDownload is completed successfully")
