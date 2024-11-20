import sqlite3

conn = sqlite3.connect("example.db")
user_input = "user_input"
query = f"SELECT * FROM users WHERE username = '{user_input}'"
conn.execute(query)
