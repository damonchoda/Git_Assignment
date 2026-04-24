from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'This is the home page of the Flask application running on Python 3.10.'
@app.route('/api/<name>')
def length(name):
    if len(name)>5:
        return f'The length of the name "{name}" is greater than 5.'
    else:       
        return f'The length of the name "{name}" is less than or equal to 5.'
if __name__ == '__main__':
    app.run(debug=True)
