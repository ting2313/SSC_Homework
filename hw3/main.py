import customer
import server
import numpy as np
AVERAGE_ARRIVE_TIME = 4
SERVING_NUM = 10

server = server.Server()
clientCreateTime = np.random.exponential(scale=AVERAGE_ARRIVE_TIME,size=SERVING_NUM)
server.start(SERVING_NUM)
