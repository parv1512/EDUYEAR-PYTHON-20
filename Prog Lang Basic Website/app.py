from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/python')
def python():
	return render_template('Python.html')

@app.route('/c')
def c():
	return render_template('c.html')

@app.route('/java')
def java():
	return render_template('java.html')

if __name__ == '__main__':
	app.run(debug=True)