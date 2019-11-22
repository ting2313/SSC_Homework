import waitingQueue
import time
import customer

class Server:
    def __init__(self):
        self.queue = waitingQueue.WaitingQueue()
        self.servingNum = 0
        self.servingTime = 0.0
    def start(self, servingNum):
        while 1:
            if self.servingNum==servingNum :
                break
            if(self.queue.getListLen()!=0):
                servingCustomer=self.queue.pop()
                self.servingNum += 1
                print ("Start serving No.%d with %f sec" %(self.servingNum,servingCustomer.processTime))
                time.sleep(servingCustomer.processTime)
                self.servingTime += servingCustomer.processTime
        