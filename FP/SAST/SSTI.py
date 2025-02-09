from flask import Flask, render_template_string, request, escape

app = Flask(__name__)

@app.route('/safe', methods=['GET'])
def safe():
    user_input = request.args.get('name', 'Guest')

    safe_user_input = escape(user_input)

    template = "<h1>Welcome, {{ name }}</h1>"
    return render_template_string(template, name=safe_user_input)
