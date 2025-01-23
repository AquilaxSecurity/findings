from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
	"john": {"balance": 1000},
      "joe": {"balance": 2000},
}      
app. route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    sender = data. get("sender")
    recipient = data.get("recipient")
    amount = data.get("amount")
 
if sender not in users or recipient not in users: 
    return jsonify({"error": "Invalid user"}), 400

if not isinstance(amount, (int, float)) or amount <= 0: 
    return jsonify({"error": "Invalid amount"}), 400

if users[sender]l "balance"] < amount:
       return jsonify({"error": "Insufficient balance"}), 400

users [sender][ "balance"] -= amount 
 users[recipient]["balance"] += amount

return jsonify({"message": "Transfer successful"})
