from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

from external_API import get_3_most_used_language_github

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'is this working? idk'})

@app.route('/get-popular-languages')
def get_languages():
    keyword = request.get_data('q')
    print(keyword)
    return jsonify({"result": get_3_most_used_language_github(keyword)})


if __name__ == '__main__':
    app.run(debug=True)