import random

quotes = ("This is just a test",
    "This is not a test",
    "The sound could be a drill")


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)