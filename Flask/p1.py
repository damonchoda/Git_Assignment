from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello! This is a Flask application running on Python 3.10.[1st page]'
@app.route('/second')
def second():
    return 'This is the second page of the Flask application running on Python 3.10.'
@app.route('/api/<name>')
def name(name):
    print(name)
    return f'Hello, {name}! This is a dynamic route in the Flask application running on Python 3.10.'
@app.route('/porn')
def porn():
    return 'Mia Khalifa'
if __name__ == '__main__':
    app.run(debug=True)