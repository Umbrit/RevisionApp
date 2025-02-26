import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print(f"User '{username}' added successfully!")
except sqlite3.IntegrityError:
    print(f"User '{username}' already exists.")
finally:
    conn.close()
