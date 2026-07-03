import sqlite3

DB_NAME = "leadhunter.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS businesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            website TEXT,
            country TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_business(company, website, country, status="New"):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO businesses
        (company, website, country, status)
        VALUES (?, ?, ?, ?)
    """, (company, website, country, status))

    conn.commit()
    conn.close()


def get_all_businesses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT company, website, country, status
        FROM businesses
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data