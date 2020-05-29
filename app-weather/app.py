from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def default_home():
    return "Home page - weather application", 200


@app.route('/weather', methods=['GET'])
def default_weather():
    return "Il fait beau ajourd'hui", 200

# This is for debug mode on
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
