from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login_success', methods=['POST'])
def login_success():
	user_name = request.form['user_name']
	password = request.form['password']
	return render_template('success.html', user_name=user_name, password=password)

if __name__ == '__main__':
    app.run(debug = True)

# http://127.0.0.1:5000/hello?fname=A&lname=B
