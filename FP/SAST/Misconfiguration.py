from flask import Flask, request, render_template, jsonify
import sqlite3
import bcrypt
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_strong_secret_key'
csrf = CSRFProtect(app) 

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT UNIQUE, 
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def check_credentials(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    stored_password = cursor.fetchone()
    conn.close()

    if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0].encode('utf-8')):
        return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_credentials(username, password):
            return render_template('success.html')
        else:
            return render_template('failure.html')
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return "Admin access is restricted."

@app.route('/add_user', methods=['POST'])
@csrf.exempt  # If using API, exempt CSRF but use token-based auth instead
def add_user():
    username = request.form['username']
    password = request.form['password']

    if not username or not password or len(password) < 8:
        return jsonify({"error": "Invalid input"}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password.decode('utf-8')))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409 

    return jsonify({"message": "User added successfully"}), 201

# Secure Users Route
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username FROM users') 
    users = cursor.fetchall()
    conn.close()
    
    user_list = [{"id": user[0], "username": user[1]} for user in users]
    
    return jsonify({"users": user_list})