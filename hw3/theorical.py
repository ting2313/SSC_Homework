import matplotlib.pyplot as plt

class Calculator:
    def __init__(self,arrivalRate,serviceRate):
        self.arrivalRate = arrivalRate
        self.serviceRate = serviceRate
        self.utilization = arrivalRate/serviceRate
        self.customerLine = self.utilization*self.utilization/(1-self.utilization)
        self.customerSystem = self.customerLine+self.utilization
        self.waitingTime = self.utilization/(serviceRate-arrivalRate)
        self.systemTime = self.waitingTime+ 1/serviceRate
    def stateRate(self, num):
        x = []
        y = []
        for i in range(0,num+1):
            x.append(i)
            y.append(pow(self.utilization,i)*(1-self.utilization))
        plt.bar(x,y,width=0.8)
        plt.title("Theorical Rate")
        plt.show()
    def print(self):
        print("[Theorical Value]")
        print("Average time in line:%f"%(self.waitingTime))
        self.stateRate(30)
