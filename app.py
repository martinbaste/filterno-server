from flask import Flask, render_template, request;
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/analyze')
def analyze():
    return request.args.get('text');