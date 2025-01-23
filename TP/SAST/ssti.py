from flask import Flask, request
app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    return f"Hello, {username}!"

if __name__ == '__main__':
    app.run()
