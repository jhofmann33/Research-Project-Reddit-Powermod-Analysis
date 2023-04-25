import csv
import matplotlib.pyplot as plt
import numpy as np

setForAnalysis = "../Powers/100Power.csv"

loadIn = []
dataAll = {i: 0 for i in range(0, 400000000, 1000000)}
with open(setForAnalysis, 'r') as csv_file:   
    csv_reader = csv.reader(csv_file)
    # Count the number of names in each category
    for row in csv_reader:
        loadIn.append(row)

for row in loadIn[1:]:
    #print(row)
    name = row[0]
    value = int(row[1])
    for x in range(0, 400000000, 1000000):
        if x <= value < x + 1000000:
            dataAll[x] += 1

newSet = {}
for entry in dataAll:
    #print(entry)
    if entry < 300000000:
        if dataAll[entry] > 0:
            newSet[entry] = dataAll[entry]
        



#Plot 1-----Scatter
#plt.scatter(dataAll.keys(), dataAll.values(), s=10)
plt.scatter(newSet.keys(), newSet.values(), s=3)
plt.xlabel('Mod Influence by Hundreds of Millions of Users')
plt.ylabel('Number of Moderators')
plt.show()
#Plot 2-----Log(Scatter)
plt.scatter(np.log10(list(newSet.keys())), np.log10(list(newSet.values())), s=10)
plt.xlabel('Log(Scope of Reach in Groups by Millions)')
plt.ylabel('Log(Number of Moderators in Category)')
plt.show()


