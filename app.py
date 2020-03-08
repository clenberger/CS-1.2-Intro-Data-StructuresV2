from flask import Flask, render_template
from generate_sentence import generate_sentence
import os
from book import book
from markov import MarkovChain

app = Flask(__name__)

@app.route('/')
def index():
        
    my_list = book('words.txt')
    chain = MarkovChain(my_list)
    num_words = int(10) - 1
    my_sentence = chain.walk(num_words)


    return render_template('index.html', sentence=my_sentence)


if __name__ == '__main__':
    app.run(debug=True)