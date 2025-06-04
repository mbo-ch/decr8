import sqlite3

# Connect to DB (creates file if not exists)
conn = sqlite3.connect("decr8.db")
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
conn.close()
