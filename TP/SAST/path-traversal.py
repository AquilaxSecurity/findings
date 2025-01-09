import os
from flask import Flask, request, send_file

app = Flask(__name__)

DIR = "/var/www/html/"

@app.route("/download", methods=["GET"])
def download_file():
    
    file = request.args.get("files")

    file_path = os.path.join(DIR, file)

    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return "File is not found"


