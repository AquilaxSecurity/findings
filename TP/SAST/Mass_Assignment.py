from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated User Database
users = {
    "user1": {"username": "user1", "password": "password12", "role": "user"},
    "admin": {"username": "admin", "password": "adminrocks", "role": "admin"}
}

@app.route("/update_profile", methods=["POST"])
def update_profile():
    data = request.get_json() 
    username = data.get("username")

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    users[username].update(data)  
    return jsonify({"message": "Profile updated successfully", "user": users[username]})

if __name__ == "__main__":
    app.run(debug=True)
