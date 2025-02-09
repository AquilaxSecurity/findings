from flask import Flask, request, jsonify
from pymongo import MongoClient
from werkzeug.security import check_password_hash
import re

app = Flask(__name__)

client = MongoClient('mongodb://username:password@localhost:27129/', serverSelectionTimeoutMS=5000)
db = client['mydatabase']
collection = db['users']

def is_valid_username(username):
    """Ensure username is alphanumeric and 3-20 characters long"""
    return re.match("^[a-zA-Z0-9]{3,20}$", username)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    username = data['username']
    password = data['password']

    if not is_valid_username(username):
        return jsonify({'error': 'Invalid username format'}), 400

    user = collection.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
