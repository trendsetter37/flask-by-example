from bs4 import BeautifulSoup
import nltk
import re
import operator
from stop_words import stops
from collections import Counter

def process_text(request_object, errors, results):

    raw = BeautifulSoup(request_object.text, "html.parser").get_text()
    nltk.data.path.append('./nltk_data/')
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)

    # remove punctuation, count raw words
    nonPunct = re.compile('.*[A-Za-z].*')
    raw_words = [w for w in text if nonPunct.match(w)]
    raw_word_count = Counter(raw_words)

    # stop words
    no_stop_words = [w for w in raw_words if w.lower() not in stops and len(w) > 1]
    no_stop_words_count = Counter(no_stop_words)
    # save the results to database
    results = sorted(
     		no_stop_words_count.items(),
       		key=operator.itemgetter(1),
       		reverse=True
       	)[:10]
    try:
       	result = models.Result(
      		url=url,
       		result_all=raw_word_count,
       		result_no_stop_words=no_stop_words_count
       		)
       	db.session.add(result)
       	db.session.commit()
    except:
       	errors.append("Unable to add item to database.")

    return (errors, results)