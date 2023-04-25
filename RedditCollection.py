#Python Reddit Data Collection Mark_1
import pandas as pd
#from pandas import dataframe
from openpyxl.workbook import Workbook
import csv
import praw

#----------------
#Functions

def popularSubs():
    subList = []
    for subreddit in reddit.subreddits.popular(limit=50):
        #if str(subreddit) != 'Home': #home inclusion freezes program
        subList.append(str(subreddit.display_name))
    return subList


#Gets the moderators for every subreddit in list
def subredditScraper(subredditList):
    moderatorList = []
    progCount = 0
    for subreddit in subredditList:
        print("Prog check, new subScrap starting-----------------------" + str(progCount))
        progCount = progCount + 1 #quality of rendering wait
        temp = reddit.subreddit(subreddit).moderator()
        for moderator in temp:
            #print(moderator)
            if str(moderator) != "AutoModerator": #excluding from dataset will need updating to a list of automods
                if moderator not in moderatorList: #prevent repeats
                    moderatorList.append(str(moderator))
    return moderatorList


#Returns all subreddits moderated by a user
def modAnalysis(moderator):
    target = reddit.redditor(moderator) 
    allModerated = target.moderated()
    modOutput = [moderator] #put name before adding their subreddits
    for subreddit in allModerated:
        modOutput.append(str(subreddit))
    return modOutput






#MAIN--------------------------------------------------------------


#Setup---------DO NOT SHARE WITH OTHERS!!!!
my_client_id = 'xxx'
my_client_secret = 'xxx'
my_user_agent = 'xxx'
username = "xxx"
password = "xxx"
reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, username = username, password = password, user_agent=my_user_agent)
#---------------------------
#---------------------------
#---------------------------

#Get a list of the top subreddits----------------------------------------------------
subredditList = popularSubs()
print(subredditList)
print(len(subredditList))

#Get the user sizes from list of subreddits------------------------------------------
with open('../Sizes/1000Sizes.csv', 'w') as f2:
    for entry in subredditList:
        temp = reddit.subreddit(entry)
        size = temp.subscribers
        s = entry + ',' + str(size) + "\n"
        f2.write(s)


#Take list of moderators and export all the subreddits they moderate-----------------
moderatorList = subredditScraper(subredditList)
count = len(moderatorList)
count2 = 0
with open('50Output.csv', 'w') as f:
    for mod in moderatorList: #1 mod at a time
        print("Loop 2 Count: " +str(count2) + "/" + str(count))
        count2 = count2 + 1
        s = ','.join(str(x) for x in modAnalysis(mod))
        s = s + "\n"
        f.write(s)

    

print("Program Done!")







#Notes------------------
# https://www.reddit.com/r/memes/about/moderators.json
#could be a way to get moderators

#Program runs realllllly slowly with bigger subreddit lists

# https://www.reddit.com/prefs/apps/












