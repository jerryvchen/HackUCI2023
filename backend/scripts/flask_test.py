from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS # remove later
from flask_testApiHandler import flask_testApiHandler

app = Flask(__name__, static_url_path='', static_folder='')
CORS(app) # also remove later
api = Api(app)

@app.route('/', defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)