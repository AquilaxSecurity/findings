from flask import Flask, request
import requests
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_DOMAINS = ['example.com', 'trusted-domain.com']

def is_allowed_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc in ALLOWED_DOMAINS

@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')

    if not url:
        return "Please provide a URL parameter.", 400

    if not is_allowed_url(url):
        return "Access to the provided URL is not allowed.", 403

    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}", 500