from flask import Flask,send_file
app=Flask(__name__)
@app.route('/')
def home():
    return "This is home page"
@app.route('/api')
def api():
    return send_file('data.json',mimetype='application/json')
if __name__ == '__main__':
    app.run(debug=True)