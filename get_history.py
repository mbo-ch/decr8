from pyrogram import Client
import logging, sqlite3

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

api_id = 314504
api_hash = "8c64c308e6f0186d495ae1e92a1c228d"

decr8 = -1001280481543
decr8_v2 = -1001969042072

DB_PATH = "/home/decr8/decr8/decr8.db"

from pyrogram import Client
import sqlite3

api_id = 314504
api_hash = "8c64c308e6f0186d495ae1e92a1c228d"

DB_PATH = "/home/decr8/decr8/decr8.db"

def save_messages_to_db(channel_name, chat_id):
    with Client("get_history", api_id, api_hash) as app, sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        for msg in app.get_chat_history(chat_id):
            if msg.audio:
                is_album = 1 if getattr(msg, "media_group_id", None) else 0
                media_group_id = getattr(msg, "media_group_id", None)
                cur.execute("""
                    INSERT OR IGNORE INTO songs 
                    (channel, msg_id, performer, filename, duration, date, title, is_album, media_group_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    channel_name,
                    msg.id,
                    getattr(msg.audio, "performer", None),
                    getattr(msg.audio, "file_name", None),
                    getattr(msg.audio, "duration", None),
                    str(getattr(msg.audio, "date", None)),
                    getattr(msg.audio, "title", None),
                    is_album,
                    media_group_id,
                ))
        conn.commit()
        
if __name__ == "__main__":
    save_messages_to_db("main", decr8_v2)
    save_messages_to_db("inactive", decr8)
    logging.info("Done importing history to SQLite.")
