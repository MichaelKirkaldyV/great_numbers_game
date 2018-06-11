from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/guess', methods=['GET'])
def guess_number():
	random = random.randrange(0, 101)
	print random
	if session.get('number') == random:
		return render_template('answer.html')
	elif session['number'] <= 50:
		return render_template('too_low.html')
	else:
		return render_template('too_high.html')

app.run(debug=True) 