#######################################
# Reference:
#   stackoverflow:49947814
#######################################

import customer
import server
import theorical
import numpy as np
import time
import threading
AVERAGE_ARRIVE_TIME = 0.125
SERVING_NUM = 1000
startTime = time.time()

# Creating an object of server and start at another threading
server = server.Server(startTime)
serverThread = threading.Thread(target=server.start,args=[SERVING_NUM])
serverThread.start()
print("Create Thread Successfully")

# Creating customers which following exponential distribution
clientCreateTime = np.random.exponential(scale=AVERAGE_ARRIVE_TIME,size=SERVING_NUM-1)
newCustomer = customer.Customer()
server.queue.push(newCustomer)
lastTime = time.time()
for clientTime in clientCreateTime :
    while (time.time()-lastTime)<clientTime:
        continue
    newCustomer = customer.Customer()
    server.queue.push(newCustomer)
    lastTime = time.time()

# Waiting for the server
serverThread.join()
totalServerTime = time.time()-startTime
print("End Simulation")

# Evaluating
calculator = theorical.Calculator(1/AVERAGE_ARRIVE_TIME,1/customer.AVERAGE_SERV_TIME)
calculator.print()

print("[Experiment Value]")
print("Average Waiting Time:%f"%(server.queue.totalWaitingTime/SERVING_NUM))
print("Usage:%f"%(server.servingTime/totalServerTime))
