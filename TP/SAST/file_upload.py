from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = file.filename 
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            return f"File uploaded successfully: {file_path}"
    return '''
    <html>
        <body>
            <h2>Upload a File</h2>
            <form action="/" method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>



