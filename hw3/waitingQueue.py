import customer
import time

class WaitingQueue:
    def __init__(self, startTime):
        self.totalCustomer = 0
        self.totalWaitingTime = 0.0
        self.list = []
        self.stateTime = startTime
    def push(self, customer):
        if self.getListLen() == 0:
            customer.inqueue = False
        else:
            self.totalCustomer += 1
        self.list.append(customer)
        # print("Push at %f"%time.time())
    def pop(self):
        try:
            firstCustomer = self.list[0]
            # print("Pop at %f"%time.time())
            if firstCustomer.inqueue:
                self.totalWaitingTime += time.time()-firstCustomer.createTime
            del self.list[0]
            return firstCustomer
        except LookupError :
            print("ERROR!There is no element to pop!")
    def getListLen(self):
        return len(self.list)
    def printState(self):
        print("State %d at time %f", )

    