import csv
import matplotlib.pyplot as plt
import numpy as np
import praw

#Settings--------------------------------
setForAnalysis = "../Outputs/100Output.csv"
setSizes = "../Sizes/1000Sizes.csv" #Larger is better to reduce praw needs

#DO NOT SHARE!!!-------------------------------
my_client_id = 'xxx'
my_client_secret = 'xxx'
my_user_agent = 'xxx'
username = "xxx"
password = "xxx"
reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, username = username, password = password, user_agent=my_user_agent)
#----------------------------------------------




#Update this soon to be from a established list
#Filter List------------------------------------
botList = ['AssistantBOT1','modmail_bot', 'BotDefense', 'MAGIC_EYE_BOT', 'DuplicateDestroyer', 'AssistantBOT', 'BotTerminator', 'RepostSleuthBot']
whitelist = ['sloth_on_meth'] #for debigging



#Get Subreddit Size Data Loaded----------------
setData = {}
with open(setSizes, 'r') as csv_file:   
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        subreddit = row[0]
        volume = int(row[1])
        setData[subreddit] = volume

with open('50Power.csv', 'w') as f: #print line each iteration
    writer = csv.writer(f)
    writer.writerow(['Moderator', 'Power'])
#Total Mods with their subreddit sizes--------------
    dataAll = {}
    errors = {}
    with open(setForAnalysis, 'r') as csv_file:   
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            name = row[0]
            dataAll[name] = 0
            subreddits = row[1:]
            if name not in botList: #Bot filter
            #if name in whitelist: ##debug
                #target = reddit.redditor(name) ##debug
                #allModerated = target.moderated()##debug
                #print(allModerated) ##debug
                for entry in subreddits:
                    #print(entry)
                    try:
                        if entry not in setData: #If not already loaded then do so
                            a = reddit.subreddit(entry)
                            b = a.subscribers
                            setData[entry] = b            
                        temp = int(dataAll[name]) # save current value
                        size = int(setData[entry]) # get entries size
                        dataAll[name] = temp + size #update data
                    except: #logging errors
                        try:
                            errors[name].append(entry)
                        except KeyError:
                            errors[name] = [entry]
                print("Mod: " + name + ", Power: " + str(dataAll[name]))
                writer.writerow([name, dataAll[name]])
    #print(dataAll)
print("-------ERRORS--------")
print(errors)
            








