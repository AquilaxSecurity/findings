from flask import Flask, request, redirect, url_for, abort

app = Flask(__name__)

ALLOWED_DOMAINS = ["yourdomain.com", "localhost"]

@app.route('/redirect', methods=['GET'])
def redirect_url():
    host = request.headers.get('Host', '')

    if not any(allowed in host for allowed in ALLOWED_DOMAINS):
        abort(400, "Invalid Host Header")

    return redirect(url_for('admin_dashboard'), code=302)

@app.route('/admin')
def admin_dashboard():
    return "Welcome to the Admin Dashboard"
