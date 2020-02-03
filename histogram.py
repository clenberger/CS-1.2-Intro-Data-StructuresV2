import sys
import re

words_file = 'words.txt'

def book(words_file):
    '''Opens text file and arranges words into a readable list '''
    with open (words_file, 'r') as f:
        words = f.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
    return scrubbed_words.split(" ")


def histogram(words_list):
    '''Takes text argument and returns a histogram data structure in a dictionary form'''
    histogram = {}
    for word in words_list:
        if word.lower() in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def histogram_list(words_file):
    '''histogram returns list'''
    words = book(words_file)
    histogram = []
    for word in words:
        for item in histogram:
            if item[0] == word:
                item[1] += 1
                break
        else: histogram.append([word, 1])
    return histogram

def histogram_tuples(words_file):
    '''histogram returns tuples'''
    words = histogram_list(words_file)
    histogram = []

    for item in words:
        histogram.append(tuple(item))

    return histogram


def unique_words(words_file):
    ''' returns the total count of unique words in the histogram '''
    histogram = {}

    words = book(words_file)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1
    print(len(histogram))

def frequency(search, words_file):
    histogram = {}
    words = book(words_file)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1
    print (histogram.get(search, 0))

def stochastic_sampling(histogram):
    pass

if __name__ == '__main__':
    unique_words(words_file)
    frequency('the', words_file)