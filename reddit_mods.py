import pandas as pd
import math
import praw

top100all_network = pd.read_excel("./Top100Subreddits.xlsx")
top1000all_network = pd.read_excel("./Top1000Subreddits.xlsx")

# Takes in the network and the name of the file to write to and finds the number of subreddits that all of the moderators
# in the network moderate. It will write to an excel file with the first column being the moderator name and the second
# column being the number of subreddits they moderate.
def moderators_per_subreddit(network, name):
    mods = {'ModName': [], 'NumSubreddits': []}
    column_count = network.shape[1]
    # Need to go through all of the rows in the network
    for ind in network.index:
        mods['ModName'].append(network[0][ind])
        # Need to go through all the columns in the network
        for ind2 in range(1, column_count+1):
            # try-except is necessary if values are nan
            try:
                if pd.isna(network[ind2][ind]):
                    mods['NumSubreddits'].append(ind2-2)
                    break
                elif ind2 == (column_count):
                    mods['NumSubreddits'].append(ind2-1)
            except:
                if ind2 == (column_count):
                    mods['NumSubreddits'].append(ind2-1)
    # creates the pandas dataframe of the mod data
    df = pd.DataFrame(mods)
    df.to_excel("./" + name + ".xlsx")

# Takes in the network and the name of the file to write to and finds the number of moderators present for that subreddit
# in the network. Note that when given top 100 or top 1000, it will also do this for the subreddits not within the top 100 or top 1000,
# however since the moderator list only contains the moderators respective to the top 100 or 1000, it will be a lower number than their
# actual moderators and only show the number of moderators who moderate in the top 100 or 1000 that also moderate in those subreddits.
def subreddit_mod_count(network, name):
    subreddits = {}
    row_count = network.shape[0]
    column_count = network.shape[1]
    # Go through each row
    for ind in network.index:
        # Go through each column
        for ind2 in range(1, column_count+1):
            # try-except is needed in case of a nan value
            try:
                if pd.isna(network[ind2][ind]):
                    break
                else:
                    if network[ind2][ind] in subreddits:
                        subreddits[(network[ind2][ind])] = subreddits[(network[ind2][ind])] + 1
                    else:
                        subreddits[(network[ind2][ind])] = 1
            except:
                # break is here since if we hit a nan value we have no more subreddits for that moderator
                break
    subreddit_counts = {'SubredditName': [], 'ModCount': []}
    for key in subreddits.keys():
        subreddit_counts['SubredditName'].append(key)
        subreddit_counts['ModCount'].append(subreddits[key])
    # creates the pandas dataframe of the subreddit data
    df = pd.DataFrame(subreddit_counts)
    df.to_excel("./" + name +".xlsx")

# takes in a network and the list of the top subreddits and the count of that list
# and goes through the network and sums up the total moderators without unique values
def total_mods_n(network, top_list, top_count):
    subreddits = {}
    column_count = network.shape[1]
    # Go through the rows
    for ind in network.index:
        # Go through the columns
        for ind2 in range(1, column_count+1):
            # need try-except for nan values
            try:
                if pd.isna(network[ind2][ind]):
                    break
                else:
                    if (network[ind2][ind] not in subreddits) and (network[ind2][ind] in top_list):
                        subreddits[(network[ind2][ind])] = 1
                    elif (network[ind2][ind] in subreddits) and (network[ind2][ind] in top_list):
                        subreddits[(network[ind2][ind])] += 1
            except:
                break
    # add up the total mods
    total_mods = 0
    for key in subreddits.keys():
        total_mods += subreddits[key]
    return total_mods

# mod_stats takes a network and the amount of top subreddits of that network and then
# prints a bunch of mod stats about that network, see the print statements for information about what is printed.
def mod_stats(network, top_subreddit_count):
    row_count = network.shape[0]
    column_count = network.shape[1]
   
    # get the list of mods and their number of subreddits
    mods = {'ModName': [], 'NumSubreddits': []}
    for ind in network.index:
        mods['ModName'].append(network[0][ind])
        for ind2 in range(1, column_count+1):
            try:
                if pd.isna(network[ind2][ind]):
                    mods['NumSubreddits'].append(ind2-2)
                    break
                elif ind2 == (column_count):
                    mods['NumSubreddits'].append(ind2-1)
            except:
                if ind2 == (column_count):
                    mods['NumSubreddits'].append(ind2-1)

    # get the list of subreddits and their mod counts
    subreddits = {}
    for ind in network.index:
        for ind2 in range(1, column_count+1):
            try:
                if pd.isna(network[ind2][ind]):
                    break
                else:
                    if network[ind2][ind] in subreddits:
                        subreddits[(network[ind2][ind])] = subreddits[(network[ind2][ind])] + 1
                    else:
                        subreddits[(network[ind2][ind])] = 1
            except:
                break
    subreddit_counts = {'SubredditName': [], 'ModCount': []}
    # find the subreddits with the most mods and the amount of mods they have
    most_mods = None
    most_mods_name = []
    for key in subreddits.keys():
        if most_mods == None:
            most_mods = subreddits[key]
            most_mods_name = [key]
        elif subreddits[key] == most_mods:
            most_mods_name.append(key)
        elif subreddits[key] > most_mods:
            most_mods = subreddits[key]
            most_mods_name = [key]
        subreddit_counts['SubredditName'].append(key)
        subreddit_counts['ModCount'].append(subreddits[key])

    # sum up all moderators of all the subreddits that are not unique, so if a mod moderates 3 subreddits, theyre counted 3 times.
    all_subreddits_mod_count = sum(subreddit_counts['ModCount'])
    # determine how many unique subreddits are added per moderator.
    new_subreddits_per_mod_count = round(len(subreddits)/(len(mods['ModName'])), 2)
    avg_subreddits_per_mod = round(all_subreddits_mod_count/(len(mods['ModName'])), 2)

    print("The top " + str(top_subreddit_count) + " subreddits have a total of " + str(len(mods['ModName'])) + " moderators.")
    print("The " + str(len(mods['ModName'])) + " moderators " + "of the top " + str(top_subreddit_count) + " subreddits moderate a total of " + str(len(subreddits)) + " different subreddits.")
    print("The subreddits with the most mods of all the mods from the top " + str(top_subreddit_count) + " have: " + str(most_mods) + " moderators and are: " + str(most_mods_name))
    print("The total amount of moderators across all " + str(len(subreddits)) + " different subreddits is " + str(all_subreddits_mod_count))
    print("The average amount of new subreddits introduced by a moderator is " + str(new_subreddits_per_mod_count))
    print("The average amount of subreddits per mod is " + str(avg_subreddits_per_mod))
                
if __name__ == "__main__":
    moderators_per_subreddit(top100all_network, "Top100AllModSubCount")
    subreddit_mod_count(top100all_network, "Top100AllModCount")
    mod_stats(top100all_network, 100)
    moderators_per_subreddit(top1000all_network, "Top1000AllModSubCount")
    subreddit_mod_count(top1000all_network, "Top1000AllModCount")
    mod_stats(top1000all_network, 1000)

