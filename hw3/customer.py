import numpy as np
import time
AVERAGE_TIME = 3

class Customer:
    def __init__(self):
        self.processTime = np.random.exponential(scale=AVERAGE_TIME)
        self.createTime = time.time()