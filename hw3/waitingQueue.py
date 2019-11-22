import customer
import time

class WaitingQueue:
    def __init__(self):
        self.totalCustomer = 0
        self.totalWaitingTime = 0.0
        self.list = []
    def push(self, customer):
        self.totalCustomer += 1
        self.list.append(customer)
    def pop(self):
        try:
            firstCustomer = self.list[0]
            self.totalWaitingTime += time.time()-firstCustomer.createTime
            del self.list[0]
            return firstCustomer
        except LookupError :
            print("ERROR!There is no element to pop!")
    def getListLen(self):
        return len(self.list)

    