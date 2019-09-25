import csv
import matplotlib.pyplot as plt
import numpy as np

x = []
mean = []
middle = []
deviation = []

with open('TrainingData_new.csv',newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    
    data = []
    for num in range(1,521):
        data.append([])
        x.append(num)
    for row in rows:
        for num in range(1,521) :
            key = 'WAP%03d' % num
            data[num-1].append(int(row[key]))

    for num in range(0,520) :
        mean.append(np.mean(data[num]))
        middle.append(np.median(data[num]))
        deviation.append(np.std(data[num]))

fig,ax=plt.subplots(figsize=(20,10))
plt.plot(x,mean,'r^-',x,middle,'g^-',x,deviation,'b^-')
plt.legend(['mean','middle','standard deviation'])
plt.title("Q3")
plt.xlabel("No. of WAP")
fig.autofmt_xdate()
plt.show()