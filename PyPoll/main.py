#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")
#election_csv


# In[2]:


with open(election_csv, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    header = next(csvreader)
    print(f"CSV Header: {header}")
    
    # Read each row of data after the header
# The total number of votes cast
    total_votes = 0
    voter_index = []
    candidateVotes = {}
    for row in csvreader:
        candidateName = row[2]
        voter_index.append(row[0])
        total_votes += 1
#The total number of votes each candidate won        
        if candidateName not in candidateVotes.keys():
            candidateVotes[candidateName] = 1
        else:
            candidateVotes[candidateName] += 1

   # print(total_votes)
   # print(candidateVotes)


# In[3]:


#The percentage of votes each candidate won
    candidateVotePercentage = {}
    for candidateName in candidateVotes.keys():
        percentage = (candidateVotes[candidateName]/total_votes)*100
        candidateVotePercentage[candidateName] = percentage

    #print(candidateVotePercentage)


# In[4]:


#The winner of the election based on popular vote.
    winningCandidate = sorted(candidateVotes, key=candidateVotes.get, reverse=True)[0]


# In[5]:


print("Election Results")
print("")
print("Total Votes: "+str(total_votes))
print("-------------------------")

for candidateName in sorted(candidateVotes, key=candidateVotes.get, reverse=True):
    print(candidateName + ": " + str(round(candidateVotePercentage[candidateName], 3))+"% "+"(" + str(candidateVotes[candidateName])+")")

print("-------------------------")
print("Winner: " + winningCandidate)
print("-------------------------")


# In[6]:


# Create the path for the filename
election_results = os.path.join(".." , "Resources", "election_results.csv")

# Write data to a .csv file
with open(election_results, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # To save specific data input as a row in the csv
    writer.writerow(["Election Results"])
    writer.writerow([""])
    writer.writerow(["Total Votes: "+str(total_votes)])
    writer.writerow(["-------------------------"])
    for candidateName in sorted(candidateVotes, key=candidateVotes.get, reverse=True):
        writer.writerow([candidateName + ": " + str(round(candidateVotePercentage[candidateName], 3))+"% "+"(" + str(candidateVotes[candidateName])+")"])
    writer.writerow(["-------------------------"])
    writer.writerow(["Winner: " + winningCandidate])
    writer.writerow(["-------------------------"])


# In[ ]:




