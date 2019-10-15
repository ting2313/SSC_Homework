import random
import numpy as np

# Do one times of experience
# and return the value of N
def N_generate():
    sum = 0
    N = 0   # number of U(0,1)
    while sum<=1:
        N += 1
        sum += random.random()
    return N

# Generating n times of experience
# and computing their mean and variance
def N_expect_estinate(n):
    sample = []
    for x in range(n):
        sample.append(N_generate())
    print("E[%d]:%f(var=%f)"%(n,np.mean(sample),np.var(sample)))

# Q1
N_expect_estinate(100)
# Q2
N_expect_estinate(1000)
# Q3
N_expect_estinate(10000)