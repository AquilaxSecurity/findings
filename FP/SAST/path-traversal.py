import os
from flask import Flask, request, send_file, abort

app = Flask(__name__)

SAFE_DIR = "/var/www/html/uploads"  # Restrict files to this directory
ALLOWED_EXTENSIONS = {"txt", "jpg", "png", "pdf", "docx"}  # Allowed file types

def is_safe_path(base_path, user_input):
    abs_path = os.path.abspath(os.path.join(base_path, user_input))
    return os.path.commonpath([base_path]) == os.path.commonpath([base_path, abs_path])

@app.route("/download", methods=["GET"])
def download_file():
    filename = request.args.get("files")

    if not filename:
        return abort(400, "Missing 'files' parameter.")

    if not is_safe_path(SAFE_DIR, filename):
        return abort(403, "Access denied.")

    file_path = os.path.join(SAFE_DIR, filename)

    if "." in filename and filename.rsplit(".", 1)[1].lower() not in ALLOWED_EXTENSIONS:
        return abort(403, "File type not allowed.")

    if os.path.exists(file_path) and os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return abort(404, "File not found.")