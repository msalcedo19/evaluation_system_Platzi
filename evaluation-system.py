from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
import json
import os
dirname = os.path.dirname(__file__)

path_data = os.path.join(dirname, "data.json")
app = Flask(__name__, static_folder='frontend/dist/spa', static_url_path='')
CORS(app)
with open(path_data) as file:
    data = json.loads(file.read())


@app.route("/evaluations/get_all", methods=['GET'])
@cross_origin()
def get_all_evaluations():
    return data


@app.route("/evaluations/get/<id>", methods=['GET'])
@cross_origin()
def get_evaluation(id):
    return data[id]


@app.route('/')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()