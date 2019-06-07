import csv
import os

# Load the csv file and write code for output results
file_loaded = "election_data.csv"
file_output = "Election_Poll_Analysis.txt"

#Creating variables from existing data
Total_num_votes = 0
num_voters = 0

max_votes = -1
candidate_list = []
candidate_polls = {}

# read the  file 
with open(file_loaded) as polldata:
    reader = csv.DictReader(polldata)

    for row in reader:
        candidate_current = row['Candidate']
        if candidate_current not in candidate_list:
            num_voters = num_voters+1
            candidate_list.append(candidate_current)
            candidate_polls[candidate_current]=0

        candidate_polls[candidate_current] = candidate_polls[candidate_current] +1
        Total_num_votes = Total_num_votes +1

        if candidate_polls[candidate_current] > max_votes:
            max_votes = candidate_polls[candidate_current]
            candidate_winner = candidate_current

output = 'Election Results\n-----------------\nTotal Votes: %d\n----------------- %(Total_num_votes)'

for name in candidate_list:

    results = ('  %s: %.3f%% (%d)' %(name,  100*candidate_polls[name]/(0.0+Total_num_votes), candidate_polls[name]))
    output = output + '\n' + results

#print the final result/winner of the election
final_output = output + '\n-----------------n  Winner: %s\n-----------------n' %(candidate_winner)
print(final_output)
with open(file_output, "w") as outputfile:
    outputfile.write(final_output)