#######################################
# Reference:
#   stackoverflow:49947814
#######################################

import customer
import server
import numpy as np
import time
import threading
AVERAGE_ARRIVE_TIME = 4
SERVING_NUM = 10

# Creating an object of server and start at another threading
server = server.Server()
serverThread = threading.Thread(target=server.start,args=[SERVING_NUM])
serverThread.start()
print("Create Thread Successfully")

# Creating customers which following exponential distribution
startTime = time.time()
clientCreateTime = np.random.exponential(scale=AVERAGE_ARRIVE_TIME,size=SERVING_NUM)
for clientTime in clientCreateTime :
    while (time.time()-startTime)<clientTime:
        continue
    newCustomer = customer.Customer()
    server.queue.push(newCustomer)

# Waiting for the server
serverThread.join()
totalServerTime = time.time()-startTime
print("End Simulation")

# Evaluating
print("Average Waiting Time:")
print(server.queue.totalWaitingTime/SERVING_NUM)
print("Usage:")
print(server.servingTime/totalServerTime)
