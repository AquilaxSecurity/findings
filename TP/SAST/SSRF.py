import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')

    if not url:
        return "Please provide a URL parameter.", 400

    try:
        # Make a request to the provided URL
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)