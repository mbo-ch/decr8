import sqlite3

DB_PATH = "/home/decr8/decr8/decr8.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS songs (
    channel TEXT,
    msg_id INTEGER,
    performer TEXT,
    filename TEXT,
    duration INTEGER,
    date TEXT,
    title TEXT,
    is_album INTEGER DEFAULT 0,        -- 0 = normal, 1 = part of album/grouped media
    media_group_id TEXT DEFAULT NULL,  -- stores group/album ID if present
    PRIMARY KEY (channel, msg_id)
)
""")
conn.commit()
conn.close()

print("Table 'songs' created (or already exists).")
