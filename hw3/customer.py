import numpy as np
import time
AVERAGE_SERV_TIME = 0.1

class Customer:
    def __init__(self):
        self.processTime = np.random.exponential(scale=AVERAGE_SERV_TIME)
        self.createTime = time.time()
        self.inqueue = True
