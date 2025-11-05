from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from rame4494 in 3308!'
