from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/test')
def mainpage():
    name = 'Matie'
    return render_template('index.html', name=name)


@app.route('/')
def hello_world():
    return 'hello world'



