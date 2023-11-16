import sqlite3


def get_random_text():
    conn = sqlite3.connect('texts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT text FROM texts ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


def add_text(text: str):
    conn = sqlite3.connect('texts.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO texts VALUES (?)", (text,))
    conn.commit()
    conn.close()
