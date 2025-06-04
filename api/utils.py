from api.imports import *
from api.variables import *

def get_song_count(channel):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM songs WHERE channel=?", (channel,))
        return cur.fetchone()[0]

def get_random_song_list(channel, count=10):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT channel, msg_id, performer, filename, duration, date, title, is_album, media_group_id \
FROM songs WHERE channel=? ORDER BY RANDOM() LIMIT ?",
            (channel, count)
        )
        return cur.fetchall()
    
def get_song_by_channel_and_msg_id(channel, msg_id):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT channel, msg_id, performer, filename, duration, date, title, is_album, media_group_id \
FROM songs WHERE channel=? AND msg_id=?",
            (channel, msg_id)
        )
        return cur.fetchone()

def get_songs_by_media_group_id(channel, media_group_id):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT channel, msg_id, performer, filename, duration, date, title, is_album, media_group_id "
            "FROM songs WHERE channel=? AND media_group_id=? ORDER BY msg_id ASC",
            (channel, media_group_id)
        )
        return cur.fetchall()

def get_long_songs(channel, count=10):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT channel, msg_id, performer, filename, duration, date, title, is_album, media_group_id "
            "FROM songs WHERE channel=? AND duration >= ? ORDER BY RANDOM() LIMIT ?",
            (channel, 600, count)
        )
        return cur.fetchall()

def get_available_channels():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT channel FROM songs")
        rows = cur.fetchall()
    # Returns a list of channel names
    return [row[0] for row in rows]

def search_filenames(query_text):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        # Use LIKE for case-insensitive search (works for ASCII; for full Unicode, use COLLATE NOCASE)
        cur.execute("SELECT filename FROM songs WHERE filename LIKE ?", (f"%{query_text}%",))
        return [row[0] for row in cur.fetchall()]
