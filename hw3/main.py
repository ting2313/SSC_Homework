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
import matplotlib.pyplot as plt
AVERAGE_ARRIVE_TIME = 0.125
SERVING_NUM = 1000
startTime = time.time()
timeEachPerson = {}

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
    if server.queue.getListLen()+server.busy in timeEachPerson:
        timeEachPerson[server.queue.getListLen()+server.busy]+=clientTime
    else :
        timeEachPerson[server.queue.getListLen()+server.busy] = clientTime
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
print("Each Time per Person:")
totalTime = sum(timeEachPerson.values())
timeDensity = list(timeEachPerson.values())
for i in range(0,len(timeDensity)):
    timeDensity[i] /= totalTime

ax = plt.bar(list(timeEachPerson.keys()),timeDensity,width=0.8)
plt.title("Percentage in simulation")
plt.show()
