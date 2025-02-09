import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

user_input = "user_input"

query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (user_input,))

results = cursor.fetchall()

conn.close()
