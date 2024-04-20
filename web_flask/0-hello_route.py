#!/usr/bin/python3
"""starts a Flask web application port 5000"""
from flask import Flask
app = Flask(__name__)




@app.route("/", strict_slashes=False)
def hello():
    """print hello bnb"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """if main"""
    app.run(host='0.0.0.0', port=5000)
