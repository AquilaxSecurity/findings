from flask import Flask, request

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "123456"

@app.route('/')
def home():
    return "Welcome to the application"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == USERNAME and password == PASSWORD:
        return "Login successful!"
    else:
        return "Invalid credentials!"
