from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/success', methods=['POST'])
def success():
    return render_template('submit_success.html')

if __name__ == '__main__':
    app.run(debug = True)
