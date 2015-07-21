from flask import Flask
from config import *
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from models import Result

#Print config vars
#for set in app.config:
#    print "{}: {}".format(set, app.config[set])

@app.route('/')
def hello():
    return "Hello World"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
