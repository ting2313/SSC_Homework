class Calculator:
    def __init__(self,arrivalRate,serviceRate):
        self.arrivalRate = arrivalRate
        self.serviceRate = serviceRate
        self.utilization = arrivalRate/serviceRate
        self.customerLine = self.utilization*self.utilization/(1-self.utilization)
        self.customerSystem = self.customerLine+self.utilization
        self.waitingTime = self.utilization/(serviceRate-arrivalRate)
        self.systemTime = self.waitingTime+ 1/serviceRate
    def print(self):
        print("[Theorical Value]")
        print("Average time in line:%f"%(self.waitingTime))