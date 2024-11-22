import sqlite3

def setup_database():
    print("Starting database setup")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL, 
    password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    print("Database setup is complete")

if __name__ == "__main__":
    setup_database()
        