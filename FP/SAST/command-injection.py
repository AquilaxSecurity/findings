import subprocess 
import shlex
from flask import Flask, request, jsonify

app = Flask(_name_)

@app. route("/ping", methods=["GET"])
def ping():
       list = request.args.get("list")

       secure = shlex-quote(list)

       command = ["ping", "-c", "5", secure]
       result = subprocess.check_output(command, universal_newlines=True)

       return jsonify({"message": result})
