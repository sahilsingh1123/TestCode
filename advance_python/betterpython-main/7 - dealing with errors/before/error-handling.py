from flask import Flask, abort, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"
