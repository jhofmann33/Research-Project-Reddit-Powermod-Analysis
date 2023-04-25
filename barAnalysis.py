import csv
import matplotlib.pyplot as plt
import numpy as np

setForAnalysis = "../Outputs/100Output.csv"
threshold = 1000 #size cutoff for including

dataAll = {}
outliers = []
with open(setForAnalysis, 'r') as csv_file:   
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        #print(len(row) - 1) #num of subreddits per mod
        totaled = (len(row) - 1)
        if totaled < threshold: #Bot threshold
            if totaled in dataAll:
                dataAll[totaled] += 1
            else:
                dataAll[totaled] = 1
        else:
            outliers.append(row[0]) #log their username



#Plot 1-----Scatter
plt.scatter(dataAll.keys(), dataAll.values(), s=10)
plt.xlabel('Amount of Subreddits Moderated')
plt.ylabel('Number of Moderators')
plt.show()
#Plot 2-----Log(Scatter)
plt.scatter(np.log10(list(dataAll.keys())), np.log10(list(dataAll.values())), s=10)
plt.xlabel('Log(Amount of Subreddits Moderated)')
plt.ylabel('Log(Number of Moderators)')
plt.show()
#Plot 1-----Bar
plt.bar(dataAll.keys(), dataAll.values(), width=2)
plt.xlabel('Amount of Subreddits Moderated')
plt.ylabel('Number of Moderators')
plt.show()
#Plot 4----- Log(Bar)
plt.bar(np.log10(list(dataAll.keys())), np.log10(list(dataAll.values())), width=0.5)
plt.xlim(0)
plt.xlabel('Log(Amount of Subreddits Moderated)')
plt.ylabel('Log(Number of Moderators)')
plt.show()


#Show all Outliers past threshold
print(outliers) 
