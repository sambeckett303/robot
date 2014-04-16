from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.debug = True



@app.route('/robot/go/<int:num>', methods=['POST', 'GET'])
def go(num = 1):
	numbra = num*1400
	print numbra
	return render_template('robotgo.html', number = numbra)

@app.route('/robot/square/<int:num>')
def square(num = 1):
	return render_template('robotsquare.html', number = num)

if __name__ == '__main__':

	app.run()

