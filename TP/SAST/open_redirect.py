from flask 

import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def home():

    redirect_to = request.args.get('redirect_to', '/home')

    return redirect(redirect_to)

