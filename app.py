from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return jsonify(message='Hello from the planetary API. Some planet, New some planet')

@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404

if __name__ == '__main__':
    app.run()
