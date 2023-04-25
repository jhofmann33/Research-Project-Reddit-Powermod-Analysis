import csv
import matplotlib.pyplot as plt
import numpy as np
import praw

#DO NOT SHARE!!!-------------------------------
my_client_id = 'xxx'
my_client_secret = 'xxx'
my_user_agent = 'xxx'
username = "xxx"
password = "xxx"
reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, username = username, password = password, user_agent=my_user_agent)
#----------------------------------------------
def popularSubs():
    subList = []
    for subreddit in reddit.subreddits.popular(limit=60): #lil buffer incase
        #if str(subreddit) != 'Home': #home inclusion freezes program
        subList.append(str(subreddit.display_name))
    return subList

def subredditScraper(subredditList):
    moderatorList = []
    progCount = 0
    for subreddit in subredditList:
        #print("Prog check, new subScrap starting-----------------------" + str(progCount))
        progCount = progCount + 1 #quality of rendering wait
        temp = reddit.subreddit(subreddit).moderator()
        for moderator in temp:
            #print(moderator)
            if str(moderator) != "AutoModerator": #excluding from dataset will need updating to a list of automods
                if moderator not in moderatorList: #prevent repeats
                    moderatorList.append(str(moderator))
    return moderatorList


def botRemoval(moderatorList, whiteList):
    filteredList = []
    for entry in moderatorList:
        if "bot" not in entry.lower():
            filteredList.append(entry)
        if entry in whiteList:
            filteredList.append(entry)
    return filteredList



#-----------------
blackList = ['modmail_bot', 'SafestBot', 'I_Am_A_Real_Bot', 'queuenukebot', 'AssistantBOT', 'Judgement_Bot_AITA', 'BotDefense', 'notesbot', 'PublicFreakoutsBot',
            'a-mirror-bot', 'MAGIC_EYE_BOT', 'MI-Bot', 'MI-Welcome-Bot', 'MildModBot', 'RepostSleuthBot', 'unexBot', 'AssistantBOT1', 'livestreamfailsbot', 
            'LSFBotUtilities', 'neoLSFBot', 'SecretServiceBot', 'PoliticsModeratorBot', 'YachtClubBot', 'attempt-checker-bot', 'Reports-Bot-TWAA', 'GGGCommentBot',
            'exilebot', 'botCyder', 'FloodgatesBot', 'NextFuckingLevel_Bot', 'roger_bot', 'NoStupidQuestionsBot', 'SnooRawrBot', 'BotTerminator', 'ModeratelyHelpfulBot',
            'MBWBot', 'PiracyBot', 'MinecraftModBot', 'ModeratelyUsefulBot', 'Mod_Helper_Bot', 'onepiecetaskbot', 'ELI5_BotMod', 'PCMRBot', 'rukraine-bot', 'DCSbot',
            'DCTbot', 'DCSUSLbot', 'GlobalOffensiveBot', '2soccer2bot', 'toxicmodbot', 'IndexBot', 'EuropeBot', 'KupoBot', 'RepostMasterBot', 'ChainAwayBot',
             'toxicitymodbot']
whiteList = ['immaRealBotacc', 'Robotguy39', 'definitelynotabot110', 'Portrait_Robot', 'SirRobotDeNiro', 'sarahbotts', 'ex-robot-x', 'TimoTheBot']






subredditList = popularSubs()
moderatorList = subredditScraper(subredditList)

#print(moderatorList)
print("-----------------------------")
print("-----------------------------")
print("-----------------------------")

newModList = botRemoval(moderatorList, whiteList)
#print(newModList)

print("-----------------------------")
print("-----------------------------")
print("---------DIF------")

diff_list = [x for x in moderatorList if x not in newModList]
print(diff_list)

print("-----------------------------")
print("-----------------------------")
print("---------New to check------")
diff_list2 = [x for x in diff_list if x not in blackList]
print(diff_list2)







