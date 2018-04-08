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
	url = request.args.get('url')
	res = submit_query(url.split(' '), 'tonechart')
	return res