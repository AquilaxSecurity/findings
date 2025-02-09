import os
from flask import Flask, request, send_from_directory, abort

app = Flask(__name__)

SECURE_DIR = os.path.abspath("safe_files")

os.makedirs(SECURE_DIR, exist_ok=True)

@app.route('/download', methods=['GET'])
def download():
    filename = request.args.get('file', '')

    if not filename or '/' in filename or '..' in filename:
        abort(400, "Invalid file request.")

    file_path = os.path.join(SECURE_DIR, filename)

    if not os.path.isfile(file_path) or not file_path.startswith(SECURE_DIR):
        abort(404, "File not found.")

    return send_from_directory(SECURE_DIR, filename, as_attachment=True)
