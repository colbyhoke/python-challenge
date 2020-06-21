#Colby Alexander Hoke
#UNC Data Analytics Bootcamp, June 2020
#CC-BY-SA
#--------------------------------------
#INPUT: Votes (CSV formatted with columns of Voter ID,County,Candidate)
#RETURN:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.
#OUTPUT: Print to terminal and text file in ./analysis
#--------------------------------------

import csv
import os

#Declare variables
total_votes = 0
candidate_list = []
votes_list = []
candidate_votes = {}
winner = ""

#Open the file
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #---------------------------------
    #Loop through each row in the csv
    #Find all the candidates, make a list of them
    #Count the total number of votes
    #Make a list of all votes cast to use later
    #---------------------------------
    for row in csvreader:
        total_votes += 1
        votes_list.append(row[2])
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

#---------------------------------
#Compare the two lists, count votes, and add those to a dictionary
#We'll use this dictionary to store candidates(keys) and their votes(values)
#---------------------------------
for name in candidate_list:
    #Count how many times the name appears in the votes list
    count = votes_list.count(name)
    candidate_votes[name] = count

#Let's see who won
winner = max(candidate_votes.keys(), key=(lambda k: candidate_votes[k]))

#---------------------------------
#Print analysis to terminal 
#---------------------------------
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
#This prints each candidate, the percentage of votes they won, and their total individual votes
for key, val in candidate_votes.items():
    val_percent = (val/total_votes)*100
    print(f"{key}: {round(val_percent,3)}% ({val})")           
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#---------------------------------
#Print analysis to text files
#---------------------------------
with open("analysis/election_results.txt", "w") as text_file:
    print(f"Election Results", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print(f"-------------------------", file=text_file)
    for key, val in candidate_votes.items():
        val_percent = (val/total_votes)*100
        print(f"{key}: {round(val_percent,3)}% ({val})", file=text_file)           
    print("-------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print(f"-------------------------", file=text_file)
