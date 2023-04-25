import pandas as pd
from openpyxl.workbook import Workbook
import csv
import praw
#----------------

#remove bots function
def botRemoval(moderatorList, whiteList, blackList):
    filteredList = []
    for entry in moderatorList:
        if "bot" not in str(entry).lower():
            if str(entry) not in blackList:
                filteredList.append(entry)
        if entry in whiteList:
            filteredList.append(entry)
    return filteredList

#DO NOT SHARE!!!-------------------------------
my_client_id = 'xxx'
my_client_secret = 'xxx'
my_user_agent = 'xxx'
username = "xxx"
password = "xxx"
reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, username = username, password = password, user_agent=my_user_agent)
#----------------------------------------------
#Load in gathered data
manualCollectionData = "../WebMiningData.csv"
setData = []
with open(manualCollectionData, 'r') as csv_file:   
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        setData.append(row)

whiteList = ['immaRealBotacc', 'Robotguy39', 'definitelynotabot110', 'Portrait_Robot', 'SirRobotDeNiro', 'sarahbotts', 'ex-robot-x', 'TimoTheBot']
blackList = ['AutoModerator', 'DuplicateDestroyer', 'fpmods', 'modmail_bot', 'SafestBot', 'I_Am_A_Real_Bot', 'queuenukebot', 'AssistantBOT', 'Judgement_Bot_AITA', 'BotDefense', 'notesbot', 'PublicFreakoutsBot',
            'a-mirror-bot', 'MAGIC_EYE_BOT', 'MI-Bot', 'MI-Welcome-Bot', 'MildModBot', 'RepostSleuthBot', 'unexBot', 'AssistantBOT1', 'livestreamfailsbot', 
            'LSFBotUtilities', 'neoLSFBot', 'SecretServiceBot', 'PoliticsModeratorBot', 'YachtClubBot', 'attempt-checker-bot', 'Reports-Bot-TWAA', 'GGGCommentBot',
            'exilebot', 'botCyder', 'FloodgatesBot', 'NextFuckingLevel_Bot', 'roger_bot', 'NoStupidQuestionsBot', 'SnooRawrBot', 'BotTerminator', 'ModeratelyHelpfulBot',
            'MBWBot', 'PiracyBot', 'MinecraftModBot', 'ModeratelyUsefulBot', 'Mod_Helper_Bot', 'onepiecetaskbot', 'ELI5_BotMod', 'PCMRBot', 'rukraine-bot', 'DCSbot',
            'DCTbot', 'DCSUSLbot', 'GlobalOffensiveBot', '2soccer2bot', 'toxicmodbot', 'IndexBot', 'EuropeBot', 'KupoBot', 'RepostMasterBot', 'ChainAwayBot',
             'toxicitymodbot']
        
#Totalling-------------------------------------
modsFromTopSubs = {}
for entry in setData[1:]: #for every subreddit
    try:
        modstemp = reddit.subreddit(entry[0]).moderator() #get a subreddits mod list
    except:
        print(entry)
    mods = botRemoval(modstemp, whiteList, blackList)
    amountOfMods = float(len(mods))
    totalPosts = float(entry[1]) + float(entry[10]) #total "Total Posts" columns
    #print(entry[9])
    #print(entry[18])
    moderationPercentage = ((float(entry[9]) + float(entry[18])) / 2) #average "Percent Mod Removed" columns
    totalModPower = totalPosts *  moderationPercentage
    perModPower = totalModPower / amountOfMods
    for mod in mods: #per mod of subreddit
        if mod in modsFromTopSubs: #if in list already
            temp = modsFromTopSubs[mod]
            modsFromTopSubs[mod] = temp + perModPower #update power
        else: #same but if not already seen
            modsFromTopSubs[mod] = perModPower
            
#Output----------------------------
with open('utilizedPower_Output.csv', 'w') as f: #print line each iteration
    writer = csv.writer(f)
    writer.writerow(['Moderator', 'Power'])
    for mod in modsFromTopSubs:
        print("Mod: " + str(mod) + ", Power: " + str(modsFromTopSubs[mod]))
        writer.writerow([str(mod), modsFromTopSubs[mod]])
