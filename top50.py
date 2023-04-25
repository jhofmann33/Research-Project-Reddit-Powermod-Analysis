import pandas as pd
from openpyxl.workbook import Workbook
import csv
import praw
#----------------
#Functions

def popularSubs():
    subList = []
    for subreddit in reddit.subreddits.popular(limit=50):
        subList.append(str(subreddit.display_name))
    return subList

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
#print(len(subredditList))
print("List:------------------")
for item in subredditList:
    print(item)













