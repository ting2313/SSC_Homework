import random
import numpy as np

def hits_simulation():
    # initialize
    cards = []
    for i in range(1,101):
        cards.append(i)
    random.shuffle(cards)

    hits = []
    for i in range(1,101):
        if cards[i-1]==i:
            hits.append(1)
        else:
            hits.append(0)
    return hits

def hits_exp(number):
    sample = []
    for i in range(number):
        sample.append(np.mean(hits_simulation()))
    return np.mean(sample)

def hits_var(number):
    sample = []
    for i in range(number):
        sample.append(np.var(hits_simulation()))
    return np.mean(sample)

print(hits_exp(10000))
print(hits_var(10000))    