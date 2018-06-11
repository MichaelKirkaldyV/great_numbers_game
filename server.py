from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_number():
	guess = request.form['number']
	if session.get('number') is None:
       	 session['number'] = random.randrange(0, 101)
	if session.get('number') == guess:
		 return render_template('answer.html')
	elif session.get('number') < guess:
		 return render_template('too_low.html')
	else:
		 return render_template('too_high.html')

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('number')
	return redirect('/')

app.run(debug=True) 