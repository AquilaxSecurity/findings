from flask import Flask, request, jsonify 

app = Flask(__name_) 
# Debug mode is enabled 
app.config ["DEBUG"] = True 

@app. route("/data", methods= ["GET"]) 
def get_data():
      secret_key = "hardcoded_secret_key" 
      return jsonify({"data": "Here is sensitive data!"}) 

if _name_ == "_main_": 
      app.run(host="0.0.0.0", port=5000)
