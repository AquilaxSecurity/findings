from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27129/')
db = client['mydatabase']
collection = db['users']

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = {'username': username, 'password': password}
    user = collection.find_one(query)
    if user:
        return 'Login successful'
    else:
        return 'Invalid credentials'
