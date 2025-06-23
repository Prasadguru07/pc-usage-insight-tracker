import sqlite3

def create_db():
    conn = sqlite3.connect('usage_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usage (
            app_name TEXT,
            start_time TEXT,
            end_time TEXT,
            duration INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_usage(app_name, start, end, duration):
    conn = sqlite3.connect('usage_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO usage VALUES (?, ?, ?, ?)", (app_name, start, end, duration))
    conn.commit()
    conn.close()
