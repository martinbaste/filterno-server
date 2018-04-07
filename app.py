from flask import Flask, render_template, request;
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    return '{"text":"' + request.args.get('text') + '"}';