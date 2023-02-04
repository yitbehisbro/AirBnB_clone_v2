#!/usr/bin/python3
""" Run the first flask """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Return the text """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def do_hbnb():
    """ Displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def do_with_variable(text):
    """ Displays with variable """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<string:text>', strict_slashes=False)
def do_with_variable2(text):
    """ Displays with variable and path handling """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def do_with_variable3(n):
    """ Displays the text if the path variable is integer """
    text = "{} is a number".format(n)
    return text


@app.route('/number_template/<int:n>', strict_slashes=False)
def do_with_variable4(n):
    """ Displays the text if the path variable is integer """
    text = "Number: {}".format(n)
    return render_template('5-number.html', text=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
