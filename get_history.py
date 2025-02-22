from pyrogram import Client

import os, logging, json

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

##############################################
api_id = 314504
api_hash = "8c64c308e6f0186d495ae1e92a1c228d"
##############################################

decr8 = -1001280481543
decr8_v2 = -1001969042072
#### create new list/tuple for each attribute
# forwards=0
# views=0
# date=datetime.datetime()
# performer=''
# duration=0
# title=''

try:
    with open(
            "/home/decr8/res/decr8_data.json",
            "r",
            encoding="utf-8"
    ) as f:
        existing_data = json.load(f)
        with open(
                "/home/decr8/res/decr8_data.json",
                "w",
                encoding="utf-8"
        ) as f:
            json.dump(existing_data, f)
    
except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
    logging.info(e, "Creating new file...")
    with Client("get_history", api_id, api_hash) as app:
        d = {
             msg.id: {
                "performer": msg.audio.performer,
                "filename": msg.audio.file_name,
                "duration": msg.audio.duration,
                "date": str(msg.audio.date),
                "title": msg.audio.title
            }
            for msg in (app.get_chat_history(decr8))
            if msg.audio
            if not None
        }
        logging.info("Done.")
        with open(
                "/home/decr8/decr8/res/decr8_data.json",
                "w",
                encoding="utf-8"
        ) as f:
            logging.info("Writing history to json file.")
            json.dump(d, f)
            logging.info("Done.")
            
try:
    with open(
            "/home/decr8/res/decr8_data_v2.json",
            "r",
            encoding="utf-8"
    ) as f:
        existing_data = json.load(f)
        with open(
                "/home/decr8/res/decr8_data_v2.json",
                "w",
                encoding="utf-8"
        ) as f:
            json.dump(existing_data, f)
    
except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
    logging.info(e, "Creating new file...")
    with Client("get_history", api_id, api_hash) as app:
        d = {
             msg.id: {
                "performer": msg.audio.performer,
                "filename": msg.audio.file_name,
                "duration": msg.audio.duration,
                "date": str(msg.audio.date),
                "title": msg.audio.title
            }
            for msg in (app.get_chat_history(decr8_v2))
            if msg.audio
            if not None
        }
        logging.info("Done.")
        with open(
                "/home/decr8/decr8/res/decr8_data_v2.json",
                "w",
                encoding="utf-8"
        ) as f:
            logging.info("Writing history to json file.")
            json.dump(d, f)
            logging.info("Done.")
            
