from dictogram import Dictogram
from sample import sample_dict
from random import choice
from generate_sentence import generate_sentence
from book import book




class MarkovChain():
    def __init__(self, words_list):
        self.chain = {}
        for index, previous_word in enumerate(words_list):
            if index < len(words_list) - 2:
                current_word = words_list[index+1]
                words_pair = (previous_word, current_word)
                if words_pair not in self.chain:
                        self.chain[words_pair] = Dictogram()
                next_word = words_list[index+2]
                self.chain[words_pair].add_count(next_word)


    def walk(self, num_words):
        sampled_tuple = ()
        sampled_words = []
        sampled_tuple = choice(list(self.chain.keys()))
        sampled_words.extend(sampled_tuple)
        
        for i in range(0, num_words - 2):
            sampled_word = self.chain[sampled_tuple].sample()
            sampled_words.append(sampled_word)
            second_word = sampled_tuple[1]
            new_tuple = (second_word, sampled_word)
            sampled_tuple = new_tuple

        sentence = ' '.join(sampled_words).capitalize()
        return sentence




