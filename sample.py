import random 
import sys
from histogram import histogram
from book import book


def sample_dict(hist):
    random_index = random.randint(0, sum(hist.values()))
    total = 0
    for word,count in hist.items():
        total += count
        if total >= random_index:
            return word


if __name__ == "__main__":
    text = book("words.txt")
    hist = histogram(text)
    args = sys.argv[:1]
    print(sample_dict(hist))