from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash, generate_password_hash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)

USER_DB = {
    "admin": generate_password_hash("SecurePass123!") 
}

@app.route('/')
def home():
    return "Welcome to the application"

@app.route('/login', methods=['POST'])
def login():
    data = request.json  # Use JSON instead of form data
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username in USER_DB and check_password_hash(USER_DB[username], password):
        session['user'] = username  # Store user in session
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "Logged out successfully!"}), 200
