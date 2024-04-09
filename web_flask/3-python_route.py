#!/usr/bin/python3
from flask import Flask
from flask import render_template

app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_display(text="is cool"):    
    text = text.replace('_', ' ')
    return f"C {text}"

# Both routes apply to the same method
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text="is cool"): 
    text = text.replace('_', ' ')
    return f"Python {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
