from flask import Flask
from nltk import word_tokenize
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<p>Hello, World!</p>
         <h1>Hello </h1>
        """
@app.route("/hello/")
def hello():
    return """<p>Hello, World!</p>
             <h1>Hello </h1>
            """
@app.route('/tokenize/<sentence>')
def w_tokenize(sentence):
    tokenized_word = str(word_tokenize(sentence))
    return '<p>Hello, World!</p><h1>Hello </h1> %s ' % escape(tokenized_word)


