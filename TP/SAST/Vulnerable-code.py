from flask import Flask, request, jsonify
app = Flask(__name__)

users = {
    "admin": "admin",
    "user": "password"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"})

@app.route('/user/data', methods=['GET'])
def user_data():
    username = request.args.get('username')
    if username:
        return jsonify({"username": username, "data": "sensitive data"})
    else:
        return jsonify({"message": "Username not provided"})

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    username = request.args.get('username')
    if username == 'admin':
        return jsonify({"message": "Welcome to the admin dashboard"})
    else:
        return jsonify({"message": "Access denied"})
