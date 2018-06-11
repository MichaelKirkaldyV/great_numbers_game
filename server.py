from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/guess', methods=['GET'])
def guess_number():
	rand_num = random.randrange(0, 101)
	if session.get('number') == rand_num:
		return redirect('answer.html')
	elif session.get('number') <= 50:
		return redirect('too_low.html')
	else:
		return redirect('too_high.html')

@app.route('/reset', methods=['GET'])
def reset():
	session.pop('number')
	return redirect('/')

app.run(debug=True) 