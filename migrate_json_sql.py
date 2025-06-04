import json
import sqlite3

# Paths
json_path_main = 'res/decr8_data_v2.json'
json_path_inactive = 'res/decr8_data.json'
db_path = 'decr8.db'

# Connect to SQLite
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    performer TEXT,
    filename TEXT,
    duration INTEGER,
    channel TEXT,
    msg_id TEXT,
    status TEXT,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def migrate(json_path, channel):
    with open(json_path, 'r', encoding='utf8') as f:
        data = json.load(f)
    for msg_id, v in data.items():
        cur.execute("""
            INSERT INTO songs (title, performer, filename, duration, channel, msg_id, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            v.get('title'), v.get('performer'), v.get('filename'), v.get('duration'),
            channel, str(msg_id), 'active'
        ))

# Migrate both channels
migrate(json_path_main, 'main')
migrate(json_path_inactive, 'inactive')

conn.commit()
conn.close()
print("Migration complete.")
