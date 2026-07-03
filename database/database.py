import sqlite3

DB_NAME = "leads.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT,
            website TEXT,
            country TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()