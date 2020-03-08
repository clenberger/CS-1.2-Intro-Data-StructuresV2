from histogram import histogram
from sample import sample_dict
from book import book
from markov import MarkovChain

def generate_sentence():
    my_text = book("words.txt")
    histo = histogram(my_text.split("\n"))
    
    sentence = ""
    num_words = 10
    for i in range(num_words):
        word = sample_dict(histo)
        sentence += " " + word
    return sentence