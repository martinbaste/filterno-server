from flask import Flask, render_template, request
from flask_cors import CORS
from utils.query_GDELT import submit_query, get_key_words
import nltk

app = Flask(__name__)
CORS(app)

nltk.data.path.append('./nltk_dependencies')

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/analyze')
def analyze():
	url = request.args.get('url')
	keywords = get_key_words(url)
	if keywords == None:
		return 'Cannot recognize article'
	res = submit_query(keywords[0], 'tonechart')
	return res

@app.route('/analyzekw')
def analyzekw():
	keywords = request.args.get('kw')
	res = submit_query(keywords.split(' '), 'tonechart')
	return res