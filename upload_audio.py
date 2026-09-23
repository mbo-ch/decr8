from pyrogram import Client
from api.variables import decr8
import os

api_id = 123456
api_hash = "api_hash"

folder_path = "/home/decr8/music"

file_path = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        # check if the file is an audio file
        if file.endswith(".mp3") or file.endswith(".wav") or file.endswith("m4a"):
            # get the file path
            file_path.append(os.path.join(root, file))
            # create a Pyrogram InputFile instance for the audio file

with Client("upload", api_id=api_id, api_hash=api_hash) as app:
    for i in file_path:
        app.send_audio(decr8, audio=i)

app.run()
