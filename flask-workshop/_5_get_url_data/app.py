from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def index(name=''):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug = True)
