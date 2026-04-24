from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def home():
    return 'This is the home page of the Flask application running on Python 3.10.'
@app.route('/api')
def func():
    name=request.values.get('name')
    age=request.values.get('age')
    result={
        'name': 'Abir',
        'age': 22
    }
    return result
if __name__ == '__main__':
    app.run(debug=True)