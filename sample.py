import random 
import sys
from histogram import histogram


def sample_dict(hist):

    total_tokens = sum(hist.values())
    rand_num = random.randint(1,total_tokens)
    total = 0
    for key, value in hist.items():
        total += value
        if total >= rand_num:
            return key