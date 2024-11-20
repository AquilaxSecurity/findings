import sqlite3

def vulnerable_sql_query(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable to SQL Injection
    cursor.execute("SELECT * FROM users WHERE username = '" + user_input + "';")
    results = cursor.fetchall()
    return results
