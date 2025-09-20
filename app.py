from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'dedication,determination,consistent and decipline is the key of success ,'

@app.route('/health')
def health():
    return 'big success waiting for you'
