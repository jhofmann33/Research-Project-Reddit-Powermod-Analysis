import csv
import matplotlib.pyplot as plt
import numpy as np

setForAnalysis = "../utilizedPower_Output.csv"

loadIn = []
#dataAll = {i: 0 for i in range(0, 100, 1)}
dataAll = {}
with open(setForAnalysis, 'r') as csv_file:   
    csv_reader = csv.reader(csv_file)
    # Count the number of names in each category
    for row in csv_reader:
        loadIn.append(row)
total = 0
x = 0
for row in loadIn[1:]:
    x = x + 1
    name = row[0]
    value = int(float(row[1]))
    total =  total + float(row[1])
    if value in dataAll:
        dataAll[value] += 1
    else:
        dataAll[value] = 1
print(total / x)
        
        



#Plot 1-----Scatter
#plt.scatter(dataAll.keys(), dataAll.values(), s=10)
plt.scatter(dataAll.keys(), dataAll.values(), s=5)
plt.xlabel('Utilized Power')
plt.ylabel('Number of Moderators in Category')
plt.show()


