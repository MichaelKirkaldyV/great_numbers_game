from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def index():
	return render_template('index.html')

#methods use post, only for forms. A normal, URL or any route is GET by default.
@app.route('/guess', methods=['POST'])
def guess_number():
	#sets the num variable of the form submitted to guess
	guess = request.form['number']
	#always use .get when getting session variables
	#sess[] is used to set variables 
	if session.get('number') is None:
		#sets random range to session
       	 session['number'] = random.randrange(0, 101)
	if session.get('number') == guess:
		 return render_template('answer.html')
	elif session.get('number') < guess:
		 return render_template('too_low.html')
	else:
		 return render_template('too_high.html')

@app.route('/reset', methods=['GET'])
def reset():
	#deletes the session, and returns to homepage where variable is set to None.
	session.pop('number')
	return redirect('/')

app.run(debug=True) 