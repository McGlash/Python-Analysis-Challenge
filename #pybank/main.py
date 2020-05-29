#modules to import and read file
import os
import csv

# Create file path (Assumes you are in the Python-challenge parent folder)
budget_file_path = os.path.join ("..", "Resources", "budget_data.csv")

#create holder lists

months = []
profit_losses = []

#Create holder variables for total calculations

total_months = 0
total = 0

#Open file, read and view file

with open(budget_file_path, "r") as budget_csvfile:
    budget_csv_read_file = csv.reader(budget_csvfile, delimiter=',')
   
    header = next(budget_csv_read_file)

    #print(header)

    for row in budget_csv_read_file:
        
        #total analysis
        total_months += 1
        total += int(row[1])

        #create lists per column
        profit_losses.append(int(row[1]))
        months.append(row[0])

#determining month-to-month change
change = []

for month in months:
    change.append(profit_losses[months.index(month)] - profit_losses[months.index(month)-1])

#remove first calculated value - not valid
change[0] = 0

#find the average change
total_change = 0

for calculated_change in change:
    total_change = total_change + calculated_change

average_change = total_change/(len(change)-1)

#determine greatest decrease/increase

greatest_decrease = 0
month_of_greatest_decrease = 0
greatest_increase = 0
month_of_greatest_increase = 0

for calculated_change_1 in change:
    if calculated_change_1 > greatest_increase:
        greatest_increase = calculated_change_1
        month_of_greatest_increase = months[change.index(calculated_change_1)]
    if calculated_change_1 < greatest_decrease:
        greatest_decrease = calculated_change_1
        month_of_greatest_decrease = months[change.index(calculated_change_1)]

#display findings on terminal

#Title
print(" ")
print ("Financial Analysis")
print("______________________")
print(" ")

#display the total findings
print(f"Total month: {total_months}")
print(f"Total: {total}")

#display the total findings
print(f"Average change: ${round(average_change, 2)}")

#display the greatest increase/decrease findings
print(f"Greatest Increase in Profits: {month_of_greatest_increase} (${round(greatest_increase, 2)})")
print(f"Greatest Decrease in Profits: {month_of_greatest_decrease} (${round(greatest_decrease, 2)})")
print("______________________")

#store findings 
title = (" " + "\n" + "Financial Analysis" + "\n" + "______________________" + "\n")
total_findings = ("Total month: " + str(total_months) + "\n" + "Total: " + str(total) + "\n")
average_findings =("Average change: $" + str(round(average_change, 2)) + "\n")
increase_findings = ("Greatest Increase in Profits: " + str(month_of_greatest_increase) + " ($" + str(round(greatest_increase, 2)) + ")" + "\n")
decrease_findings = ("Greatest Decrease in Profits: " + str(month_of_greatest_decrease) + " ($" + str(round(greatest_decrease, 2)) + ")" + "\n" + "______________________")

#defining path for output file
budget_outputfile_path = os.path.join ("..", "Analysis", "budget_output.txt")


#writing findings to text file
with open(budget_outputfile_path, "w") as budget_txt_file:
    budget_txt_file.write(title)
    budget_txt_file.write(total_findings)
    budget_txt_file.write(average_findings)
    budget_txt_file.write(increase_findings)
    budget_txt_file.write(decrease_findings)