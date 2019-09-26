import csv
import matplotlib.pyplot as plt
# lowest mean of WAP is WAP087

x = ['0','1','2']
b0 = 0
b1 = 0
b2 = 0

with open('TrainingData_new.csv',newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        if row['WAP087']!='0':
            build = row['BUILDINGID']
            if build=='0':
                b0+=1
            elif build=='1':
                b1+=1
            elif build=='2':
                b2+=1

sum = b0+b1+b2
pdf = [b0/sum,b1/sum,b2/sum]
cdf = [b0/sum,(b0+b1)/sum,1]
plt.plot(x,pdf,'b^',x,cdf,'g-')
plt.legend(['pdf','cdf'])
plt.title("Q4")
plt.xlabel("ID of building")
plt.ylabel("Number of RSSI Value")
plt.show()