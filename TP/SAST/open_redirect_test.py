from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/redirect")
def vulnerable_redirect():
    url = request.args.get('url')
    
    # Vulnerable to Open Redirect
    return redirect(url)
