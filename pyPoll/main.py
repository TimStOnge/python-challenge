# Import necessary modules
import os
import csv

# Define input path for election data
csvpath = "/Users/timst.onge/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

# Open the CSV of election data
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the first row (header)
    next(csvreader)
    # Set each variable counter to 0
    rowcount = 0
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

    # For each row in the election data:
    for row in csvreader:
        # Count the rows (total number of votes)
        rowcount = rowcount + 1
        # Add to each candidate's counter if the vote matches their name
        if row[2] == "Khan":
            khan_count = khan_count + 1
        elif row[2] == "Correy":
            correy_count = correy_count + 1
        elif row[2] == "Li":
            li_count = li_count + 1
        elif row[2] == "O'Tooley":
            otooley_count = otooley_count + 1
    
    # Create a dictionary with each candidate as a key and each vote count as the value.
    # Then, find the key of the key/value pair where the value is the maximum of the set.
    results = {'Khan': khan_count, 'Correy': correy_count, 'Li': li_count, 'Otooley': otooley_count}
    winner = max(results, key=results.get)

    # Calculate and format each candidate's percentage of the total vote
    khan_percent = '%.3f'%((khan_count/rowcount)*100)
    correy_percent = '%.3f'%((correy_count/rowcount)*100)
    li_percent = '%.3f'%((li_count/rowcount)*100)
    otooley_percent = '%.3f'%((otooley_count/rowcount)*100)


### WRITE RESULTS TO TERMINAL 

print("Election Results")
print("----------------------------")
print(f"Total Votes:  {rowcount}")
print("----------------------------")
print(f"Khan: {khan_percent}% ({khan_count})")
print(f"Correy: {correy_percent}% ({correy_count})")
print(f"Li: {li_percent}% ({li_count})")
print(f"O' Tooley: {otooley_percent}% ({otooley_count})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


### WRITE RESULTS TO TEXT FILE

output_path = "/Users/timst.onge/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_results.txt"

with open(output_path, 'w', newline='') as file:
    file.write("Election Results\n") 
    file.write("----------------------------\n") 
    file.write(f"Total Votes: {rowcount}\n") 
    file.write("----------------------------\n")
    file.write(f"Khan: {khan_percent}% ({khan_count})\n") 
    file.write(f"Correy: {correy_percent}% ({correy_count})\n") 
    file.write(f"Li: {li_percent}% ({li_count})\n")
    file.write(f"O' Tooley: {otooley_percent}% ({otooley_count})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------\n")

    file.close()