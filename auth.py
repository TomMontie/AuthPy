import bcrypt
import sqlite3

def sign_up(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("User registered successfully")
    except sqlite3.IntegrityError:
        print("Username already exists.  Choose another: ") 
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result is None:
            print("Username not found")
    else:
        stored_hash = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            print("Login successful!")
        else:
            print("Invalid credentials. Please try again.")

    conn.close()