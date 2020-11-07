from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='localhost', port=6221)

# host='127.0.0.1', port=6221
# host='localhost', port=6221