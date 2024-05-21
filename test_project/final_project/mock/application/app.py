import json
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


app_data = {}
user_id_seq = 1


@app.route("/add_id", methods=["POST"])
def create_user_id():
    global user_id_seq
    user_name = json.loads(request.data)["name"]
    if user_name not in app_data:
        app_data[user_name] = user_id_seq
        user_id_seq += 1
        return jsonify({"user_id": app_data[user_name]}), 201
    else:
        return jsonify(f'User name {user_name} already exists: id [{app_data[user_name]}]'), 400


@app.route("/get_id/<username>", methods=["GET"])
def get_user_by_name(username):
    if user_id := app_data.get(username, None):
        return jsonify({"user_id": user_id}), 200
    else:
        return jsonify({}), 404

# APP_PORT=6000 python3.10 mock/application/app.py API
# APP_PORT=5000 python3.10 mock/application/app.py UI


if __name__ == "__main__":
    host = os.environ.get('APP_HOST', '0.0.0.0')
    port = os.environ.get('APP_PORT', '5000')
    app.run(host, port)
