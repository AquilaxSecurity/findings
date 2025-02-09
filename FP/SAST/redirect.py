from flask import Flask, request, redirect, url_for

app = Flask(__name__)

SAFE_REDIRECTS = {
    "home": "/home",
    "dashboard": "/dashboard",
    "profile": "/profile"
}

@app.route('/')
def home():
 
    redirect_to = request.args.get('redirect_to', 'home')

    safe_url = SAFE_REDIRECTS.get(redirect_to, "/home")

    return redirect(safe_url, code=303)  