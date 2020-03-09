import re
import string

def book(words_file):
    '''Opens text file and arranges words into a readable list '''
    with open (words_file, 'r') as f:
        words = f.read()
        scrubbed_words = re.sub(r'[^a-zA-Z0-9\s]+', '', words).lower()
    return scrubbed_words.split(" ")