from flask import Flask, jsonify, render_template, request
import datetime
import json
import re 
from ignore.design import design

app = design.Design(Flask(__name__), __file__, 'Format Injection')

with open('items.json', 'r') as items_file:
    try:
        DATA = json.load(items_file)
    except json.JSONDecodeError:
        DATA = {}

# Input validation function
def is_valid_id(user_input):
    """Allow only alphanumeric characters and underscores to prevent injections."""
    return re.match(r"^[a-zA-Z0-9_]+$", user_input)

@app.route('/')
def index():
    id = request.args.get('id')

    if not id:
        return render_template('index.html', result="Error: ID parameter is required.")

    if not is_valid_id(id):
        return render_template('index.html', result="Error: Invalid ID format.")

    if id in DATA:
        return render_template('index.html', result=str(DATA[id]))

    timestamp = datetime.datetime.now().isoformat()  # Securely format timestamp
    msg = {"timestamp": timestamp, "message": f"Could not find item for {id}"}

    return render_template('index.html', result=json.dumps(msg, indent=2))
