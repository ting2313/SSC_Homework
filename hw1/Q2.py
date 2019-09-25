import csv
import matplotlib.pyplot as plt

x = ['<-100','[-100~-95)','[-95~-90)','[-90~-85)','[-85~-80)','[-80~-75)','[-75~-70)','[-70~-65)','[-65~-60)','[-60~-55)','[-55~-50)','[-50~-45)','[-45~-40)','[-40~-35)','[-35~-30)','[-30~-25)','[-25~-20)','[-20~-15)','[-15~-10)','[-10~-5)','[-5~-0)']
y = []

for index in range(21) :
    y.append(0)

with open('TrainingData_new.csv',newline='') as csvfile:
    rows = csv.reader(csvfile)
    next(rows,None)
    for row in rows :
        for num in row[:520] :
            if num!='0' :
                y[21-(int((-int(num))/5) + (((-int(num))%5)!=0))]+=1

fig,ax=plt.subplots(figsize=(20,10))
ax=plt.bar(x,y,width=0.8)
plt.title("Q2")
plt.xlabel("Range of RSSI")
plt.ylabel("Number of RSSI Value")
fig.autofmt_xdate()
plt.show()