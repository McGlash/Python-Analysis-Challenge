#Title
print(" ")
print ("Election Results")
print("_________________________________")

#modules to import and read file
import os
import csv

# Create file path (Assumes you are in the #pypoll folder)
poll_file_path = os.path.join("..", "Resources", "election_data.csv")

#create holder list for votes
vote = []

#Create holder variable for total votes
total_no_votes = 0

#Open file and read file
with open(poll_file_path, "r") as poll_csvfile:
    poll_csv_read_file = csv.reader(poll_csvfile, delimiter=',')
   
    header = next(poll_csv_read_file)

    for row in poll_csv_read_file:
        
        #total analysis
        total_no_votes += 1
       
        #create lists per column
        vote.append(row[2])

# total votes findings display
print(" ")
print(f"Total Votes: {total_no_votes}")
print("_________________________________")
print(" ")

#create list of candidates
candidate_list = []

for name in vote:
    if name not in candidate_list:
        candidate_list.append(name)

#create tracker list for vote count
vote_count = []

for name_1 in range(len(candidate_list)):
    vote_count.append(0)    

#count the votes per candidate
for candidate_1 in candidate_list:
    for name_2 in vote:
        if name_2 == candidate_1:
            vote_count[candidate_list.index(candidate_1)] += 1

# calculate percentage of votes
percent_votes = []

for value in vote_count:
    percent_votes.append((value/total_no_votes)*100)

#votes by candidate findings display
for candidate_2 in candidate_list:
    print(f"{candidate_2}: {round(percent_votes[candidate_list.index(candidate_2)],2)}% ({vote_count[candidate_list.index(candidate_2)]})")
print("_________________________________")
print(" ")

#determining the winner
tracker = 0
winner = 0

for value_1 in vote_count:
    if value_1 > tracker:
        tracker = value_1
        winner = candidate_list[vote_count.index(value_1)]

#winner findings display   
print(f"Winner: {winner}")
print("_________________________________")

#defining path for output file
poll_outputfile_path = os.path.join ("..", "Analysis", "election results.txt")

#writing findings to file
with open(poll_outputfile_path, "w") as poll_txt_file:
    poll_txt_file.write(" " + "\n" + "Election Results" + "\n" + "______________________" + "\n")
    poll_txt_file.write("Total Votes: " + str(total_no_votes) + "\n" + "______________________" + "\n")

    for candidate_2 in candidate_list:
        poll_txt_file.write(f"{candidate_2}: {round(percent_votes[candidate_list.index(candidate_2)],4)}% ({vote_count[candidate_list.index(candidate_2)]})\n")
    
    poll_txt_file.write("______________________" + "\n" + "winner: " + str(winner) + "\n" + "______________________")