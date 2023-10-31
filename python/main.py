from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Define the root endpoint that returns an HTML page
@app.route('/')
def hello_world():
    return '<html><body><h1>Hello, World!</h1></body></html>'

# Define a JSON endpoint that returns random data
@app.route('/random_data')
def random_data():
    data = {
        'random_number': random.randint(1, 100),
        'random_string': ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)),
        'random_boolean': random.choice([True, False]),
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)