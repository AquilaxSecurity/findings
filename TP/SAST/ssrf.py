from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/proxy', methods=['GET'])
def proxy_request():
    url = request.args.get('url')
    if url:
        import requests
        response = requests.get(url)
        return jsonify({'status': response.status_code, 'content': response.text})
    else:
        return jsonify({'error': 'URL parameter is required'}), 400
