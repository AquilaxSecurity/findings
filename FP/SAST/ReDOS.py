from flask import Flask, render_template, request, jsonify
import json, re, html

app = Flask(__name__)

SECURE_REGEX = re.compile(r'^[a-zA-Z0-9_-]{1,50}\[subscribe\]$')

def load_products():
    """Loads products securely"""
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            return json.load(f).get('products', {})
    except Exception:
        return {}

@app.route('/')
def index():
    search = request.args.get('search', '')

    if not search:
        return render_template('index.html', result='No search regex was provided!')

    if len(search) > 50:
        return render_template('index.html', result='Search query too long!')

    if SECURE_REGEX.match(search):
        return render_template('index.html', result='Only for true subscribers')

    products = load_products()
    search_escaped = html.escape(search)

    if search in products:
        return render_template('index.html', result=f'We got that! - {html.escape(products[search])}')

    return render_template('index.html', result=f'No item found for {search_escaped}!')
