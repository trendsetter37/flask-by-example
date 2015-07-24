from flask import Flask, render_template, request, jsonify
from config import *
from flask.ext.sqlalchemy import SQLAlchemy
from sanitize import sanitize
from text_processing import process_text
import requests
import json


#################
# Configuration #
#################

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

''' will need to use models."Whatever class in models" for this to work'''
#import models # fixed circular import
import models

#################
#     routes    #
#################

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


###########################
# Angular Service Backend #
###########################


@app.route('/start', methods=['POST'])
def get_url_words():
    errors = []
    results = {}
    print "Angular communicated with backend using url service"
    # get url
    # turning request json into pyobject
    data = json.loads(request.data.decode()) 
    print "Data: {}".format(data)
    url = data['url'] # getting url from python data dictionary
    print "Loaded json into data"
    if sanitize(url):
        r = requests.get(url)
        
    else:
        url = 'http://' + url; r = requests.get(url)

    print "Urls were properly sanitized"
    # Run process
    errors, results = process_text(r, errors, results)
    # need to fix results so that they are jsonifyable

    print "Results: {}".format(results) 
    json_object = jsonify(dict(results))
    print "json_object: {}".format(json_object)
    return json_object
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
