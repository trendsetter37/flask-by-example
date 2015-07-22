from flask import Flask, render_template, request
from config import *
from flask.ext.sqlalchemy import SQLAlchemy
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup
import operator
import requests
import re
import nltk


#################
# Configuration #
#################

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

''' will need to use models."Whatever class in models" for this to work'''
#import models # fixed circular import
from models import results

#################
#     routes    #
#################

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == 'POST':
        # get url that the user has entered
        try:
            url = request.form['url']
            r = requests.get(url) # shooting out a request to get html eventually
            results['raw_text'] = r.text
        except:
            errors.append("Unable to get URL. Please make sure it's valid and try again.")
        if r:
        	# text processing
        	raw = BeautifulSoup(r.text).get_text()
        	nltk.data.path.append('./nltk_data/')
        	tokens = nltk.word_tockenize(raw)
        	text = nltk.Text(tokens)

        	# remove punctuation, count raw words
        	nonPunct = re.compile('.*[A-Za-z].*')
        	raw_words = [w for w in text if nonPunct.match(w)]
        	raw_word_count = Counter(raw_words)

        	# stop words
        	no_stop_words = [w for w in raw_words if w.lower() not in stops]
        	no_stop_words_count = Counter(no_stop_words)

        	# save the results to database
        	results = sorted(
        			no_stop_words_count.items(),
        			key=operator.itemgetter(1),
        			reverse=True
        		)
        	try:
        		result = Result(
        			url=url,
        			result_all=raw_word_count,
        			result_no_stop_words=no_stop_words_count
        			)
        		db.session.add(result)
        		db.session.commit()
        	except:
        		errors.append("Unable to add item to database.")
    return render_template('index.html', errors=errors, results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
