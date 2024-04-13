#!/usr/bin/python3
'''
    Flask app
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
        Prints Hello HBNB!
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
        Prints HBNB
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_display(text="is cool"):
    '''
        Prints c <text>
    '''
    text = text.replace('_', ' ')
    return f"C {text}"


# Both routes apply to the same method
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text="is cool"):
    '''
        Prints python <text>/ is cool
    '''
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def int_display(n):
    '''
        prints number <n>
    '''
    if n.isdigit():
        return f'{n} is a number'
    else:
        return '404 not found'


@app.route('/number_template/<int:n>')
def display_number(n):
    '''
        Renders template and also number <n> is sent
    '''
    if isinstance(n, int):
        return (render_template('5-number.html', number=n))


@app.route('/number_odd_or_even/<int:n>')
def display_even_odd(n):
    if isinstance(n, int):
        n = int(n)
        n_type = 'odd'
        if n % 2 == 0:
            n_type = 'even'
        return (render_template('6-number_odd_or_even.html', number=n,
                                number_type=n_type))


@app.route('/states_list')
def display_states():
    '''
        Displays all states with id
    '''
    states = storage.all(State)
    # Get the objects from {state_id: {objects}}
    states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception=None):
    '''
        Cleanup
    '''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_states():
    '''
        Display cities and their states
    '''
    states = storage.all(State)
    # Get the objects from {state_id: {objects}} and order by name A -Z
    states = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def find_state(id=None):
    '''
        Display states  or state and cities
    '''
    states = storage.all(State).values()
    if id:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', state=state)
        # id did not match from database
        return render_template('9-states.html')
    else:
        # No id was put, return all states
        return render_template('9-states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
