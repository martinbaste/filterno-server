from flask import Flask, render_template, request
from flask_cors import CORS
from utils.query_GDELT import submit_query

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/analyze')
def analyze():
	text = request.args.get('text')
	res = submit_query(text.split(' '))
	return res