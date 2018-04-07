from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/term/<term>')
def search_term(term):
    return 'Term ' + term 