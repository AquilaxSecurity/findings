import sqlite3

conn = sqlite3.connect("example.db")
user_input = "some_input"
query = "SELECT * FROM users WHERE username = ?"
conn.execute(query, (user_input,))
