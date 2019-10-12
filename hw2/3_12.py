import random
import numpy as np

def N_generate():
    sum = 0
    N = 0
    while sum<=1:
        N += 1
        sum += random.random()
    return N

def N_expect_estinate(n):
    sample = []
    for x in range(n):
        sample.append(N_generate())
    print("E[%d]:%f"%(n,np.mean(sample)))

# Q1
N_expect_estinate(100)
# Q2
N_expect_estinate(1000)
# Q3
N_expect_estinate(10000)