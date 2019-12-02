import waitingQueue
import time
import customer

class Server:
    def __init__(self, startTime):
        self.queue = waitingQueue.WaitingQueue(startTime)
        self.servingNum = 0
        self.servingTime = 0.0
        self.busy = 0
    def start(self, servingNum):
        while 1:
            if self.servingNum==servingNum :
                break
            if(self.queue.getListLen()!=0):
                servingCustomer=self.queue.pop()
                self.busy = 1
                self.servingNum += 1
                time.sleep(servingCustomer.processTime)
                self.busy = 0
                self.servingTime += servingCustomer.processTime


        