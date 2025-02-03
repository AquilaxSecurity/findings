from flask import Flask, json, render_template, request
from ignore.design import design
import re, html
app = design.Design(Flask(__name__), __file__, 'Regular expression Denial of Service')
@app.route('/')
def index():
    search = request.args.get('search')

    if ( search is None ):
        return render_template('index.html', result='No search regex was provided!')

    with open('items.json', 'r') as items:
        products = json.load(items)['products']

        if re.search(r'^([a-zA-Z0-9_-]+)*\[subscribe\]$', search):
            return render_template('index.html', result='Only for true subscribers')

        for name in products:
            if search in name:
               return render_template('index.html', result=f'We got that! - {products[name]}')

    return render_template('index.html', result=f'No item found for {html.escape(search)}!')