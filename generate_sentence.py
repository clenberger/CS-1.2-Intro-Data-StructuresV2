from histogram import histogram
from sample import sample_dict
from book import book

def generate_sentence():
    my_text = book("words.txt")
    histo = histogram(my_text.split("\n"))
    sentence = ""
    num_words = 12
    
    for i in range(num_words):
        word = sample_dict(histo)
        sentence += " " + word
    return sentence