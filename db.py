import sqlite3
from datetime import datetime

DB_NAME = 'match.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS choices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            date TEXT NOT NULL,
            choice TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_choice(user_id, choice):
    today = datetime.now().strftime('%Y-%m-%d')
    if has_chosen(user_id, today):
        return False
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO choices (user_id, date, choice) VALUES (?, ?, ?)', (user_id, today, choice))
    conn.commit()
    conn.close()
    return True

def has_chosen(user_id, date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM choices WHERE user_id = ? AND date = ?', (user_id, date))
    result = c.fetchone()
    conn.close()
    return result is not None
