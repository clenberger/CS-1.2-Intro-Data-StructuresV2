from random import randint
import sys

filename = "/usr/share/dict/words"
my_file = open(filename, "r")
lines = my_file.readlines()

def dictonary(num_words):
    for i in range(num_words):
        random_index = randint(0, len(lines)-1)
        print(lines[random_index])
    return i

if __name__ == "__main__":
    num_words = int(sys.argv[1])
    dictonary(num_words)