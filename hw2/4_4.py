import random
import numpy as np

# This function will generate one time of simulation
# and return the total number of "hits"
def hits_simulation():
    # generate the shuffled cards
    cards = []
    for i in range(1,101):
        cards.append(i)
    random.shuffle(cards)

    # determine whether it's "hit" or not
    sum = 0
    for i in range(1,101):
        if cards[i-1]==i:
            sum += 1
    return sum

# Do "number" times of experience and return the mean and variance
def hits_exp(number):
    sample = []
    for i in range(number):
        sample.append(hits_simulation())
    return [np.mean(sample),np.var(sample)]

print(hits_exp(200000))