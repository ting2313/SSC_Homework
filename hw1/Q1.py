import csv
import matplotlib.pyplot as plt

WAP_num = []

for index in range(521) :
    WAP_num.append(0)

# count the number of detected WAPs on each row
with open('TrainingData_new.csv',newline='') as csvfile:
    rows = csv.reader(csvfile)
    next(rows,None)
    for row in rows :
        sum_of_row = 0
        for x in row[:520] :
            if x != '0' :
                sum_of_row += 1
        WAP_num[sum_of_row] += 1

plt.plot(WAP_num[:60],'bo')
plt.title("Q1")
plt.xlabel("Numbers of detected WAP on a single capture")
plt.ylabel("Count")
plt.show()