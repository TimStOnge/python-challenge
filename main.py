# Import necessary modules
import os
import csv

# Define input path for budget data
csvpath = "/Users/timst.onge/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

# Create empty lists for profits/losses values, change values, and months
profloss = []
changelist = []
monthlist = []

# Open the CSV of budget data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the first row (header)
    next(csvreader)
    # Set each variable counter to 0
    totalamount = 0
    rowcount = 0
    proflosscount = 0

    # For each row in the budget data:
    for row in csvreader:
        # Count each profit/loss cumulatively
        totalamount = totalamount + int(row[1])
        # Populate the profloss list with profit/losses values
        profloss.append(int(row[1]))
        # Populate the monthlist with months from the budget data
        monthlist.append(row[0])
        # Count the rows (total months)
        rowcount = rowcount + 1

    # Calculate the changes between consecutive profit/loss values and write them into a list
    changelist = [profloss[x+1]-profloss[x] for x in range(len(profloss)-1)]
    # Calculate the average of the changelist and format to two decimal places
    avgchange = '%.2f'%(sum(changelist) / float(len(changelist)))
    # Find the maximum and minimum change values
    greatincrease = max(changelist)
    greatdecrease = min(changelist)

    # Delete the first entry in the months list (Jan 2010). Since this is the first month, there is no
    # profit/loss change value. This also lets the monthlist and changelist to be equally sized.
    del monthlist[0]

    # Zip together the month and change lists and put them in a dictionary
    zippeddict = dict(zip(monthlist,changelist))
    
    # For every key/value pair in the dictionary: If the value matches maximum or minimum change values,
    # store the corresponding key (month) in a corresponding variable.
    for key, value in zippeddict.items():
        if greatincrease == value:
            greatincrease_month = key
        elif greatdecrease == value:
            greatdecrease_month = key


### WRITE RESULTS TO TERMINAL

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {rowcount}")
print(f"Total: {totalamount}")
print(f"Average  Change: ${avgchange}")
print(f"Greatest Increase in Profits: {greatincrease_month} (${greatincrease})")
print(f"Greatest Decrease in Profits: {greatdecrease_month} (${greatdecrease})")


### WRITE RESULTS TO TEXT FILE

output_path = "/Users/timst.onge/GWARL201811DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data_results.txt"

with open(output_path, 'w', newline='') as file:
    file.write("Financial Analysis\n") 
    file.write("----------------------------\n") 
    file.write(f"Total Months: {rowcount}\n") 
    file.write(f"Total: {totalamount}\n") 
    file.write(f"Average Change: ${avgchange}\n") 
    file.write(f"Greatest Increase in Profits: {greatincrease_month} (${greatincrease})\n")
    file.write(f"Greatest Decrease in Profits: {greatdecrease_month} (${greatdecrease})\n")

    file.close()