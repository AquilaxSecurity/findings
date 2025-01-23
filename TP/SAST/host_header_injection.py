from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirect_url():
    url = request.headers.get('Host') + '/admin'
    return redirect(url, code=302)
