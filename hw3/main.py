#######
# Reference:
#   stackoverflow:49947814
#######
import customer
import server
import numpy as np
import time
import threading
AVERAGE_ARRIVE_TIME = 4
SERVING_NUM = 5

server = server.Server()
clientCreateTime = np.random.exponential(scale=AVERAGE_ARRIVE_TIME,size=SERVING_NUM)
serverThread = threading.Thread(target=server.start,args=[SERVING_NUM])
serverThread.start()
print("Create Thread Successfully")
startTime = time.time()
print(clientCreateTime)
for clientTime in clientCreateTime :
    while (time.time()-startTime)<clientTime:
        continue
    newCustomer = customer.Customer()
    server.queue.push(newCustomer)
    print("Add Customer")

print("End Simulation")
print(server.queue.totalCustomer)

