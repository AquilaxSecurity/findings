from flask import Flask, render_template, request
import subprocess
import ipaddress
import re
from ignore.design import design

app = design.Design(Flask(__name__), __file__, 'Command Injection Prevention')

ALLOWED_METHODS = {'status', 'info', 'metrics'} 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html', result="")

    elif request.method == "POST":
        method = request.form.get("method")
        if not method:
            return render_template('index.html', result="The post parameter 'method' is missing in the request")

        if method not in ALLOWED_METHODS:
            return render_template('index.html', result="Invalid request method")

        try:
            response = subprocess.run(
                ["curl", f"http://localhost:1337/{method}"],
                text=True, capture_output=True, check=True
            )
            return render_template('index.html', result=response.stdout)
        except subprocess.CalledProcessError as e:
            return render_template('index.html', result=f"Error: {e}")

    return "Unsupported request method", 405

@app.route('/health')
def health():
    try:
        # Secure IP check with explicit allowed loopback IPs
        client_ip = request.remote_addr
        if client_ip and ipaddress.ip_address(client_ip).is_loopback:
            return "The health of the system is quite good!"
    except ValueError:
        pass 

    return "Unauthorized", 403
