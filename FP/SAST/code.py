from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecurekey'

users = {
    "admin": generate_password_hash("admin123"), 
    "user": generate_password_hash("password456")
}

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)  # Token expires in 2 hours
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            request.username = payload['username']
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username], password):
        token = generate_token(username)
        return jsonify({"message": "Login successful", "token": token})

    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/user/data', methods=['GET'])
@token_required
def user_data():
    return jsonify({"username": request.username, "data": "sensitive data"})

@app.route('/admin/dashboard', methods=['GET'])
@token_required
def admin_dashboard():
    if request.username == "admin":
        return jsonify({"message": "Welcome to the admin dashboard"})
    return jsonify({"message": "Access denied"}), 403