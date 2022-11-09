from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def my_ip():
    ip = request.headers.getlist("X-Forwarded-For")[0]

    if request.content_type == 'application/json':
        return jsonify({'ip': ip}), 200
    else:
        return f'{ip}'
