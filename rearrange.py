import random
import sys as sys
    
def rearrange():
    
    for rand_arg in args:
        randomize = random.randint(0, len(args)-1)
        random_word = args[randomize]
        print(random_word)
    return rand_arg
        
if __name__ == '__main__':
    args = sys.argv[1:]
    rearrange()