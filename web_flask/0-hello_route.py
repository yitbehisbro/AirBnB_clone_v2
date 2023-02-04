#!/usr/bin/python3
""" Run the first flask application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Return the text """
    return 'Hello HBNB!'


if __name__ == "__main__":
    """ Run the first flask application """
    app.run(host='0.0.0.0', port=5000)
