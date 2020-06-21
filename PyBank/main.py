#Analyze bank records (csv) to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" month-by-month
    #The average of the changes in "Profit/Losses" month-by-month
    #The greatest increase in profits (date and amount) month-by-month
    #The greatest decrease in losses (date and amount) month-by-month
#Prints the analysis to the terminal and a text file in ./analysis with the results.

import csv
import os

#Declare variables
first_month=True
total_months = 0
revenue_total = 0
revenue_change = 0
previous_revenue = 0
change = 0
change_dict = {}

#Open the file
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
    #---------------------------------
    #Loop through each row in the csv
    #---------------------------------
    for row in csvreader:
        #Count the lines = same as total months
        total_months += 1
        
        #Add up all of the revenue in the second column (1)
        revenue_total += int(row[1])
        
        #Convert to a currency-friendly format
        #Guidance found here: https://kite.com/python/answers/how-to-format-currency-in-python
        total_currency = "${:,.2f}".format(revenue_total)

        #Since the first month can't have a value for month-over-month change, we set the "previous" revenue and move on
        if first_month == True:
            previous_revenue = int(row[1])
            first_month=False
        else:
            #Calculate change from previous month
            change = int(row[1]) - previous_revenue
            #Add that change, and its month to a dictionary to reference later (for min, max, etc)
            change_dict[row[0]] = change
            #Set the previous amount to the current row before looping
            previous_revenue = int(row[1])

#---------------------------------
#Do work outside the loop
#---------------------------------
#Get the sum of all of the values in our change dictionary
change_values = change_dict.values()
avg_change = round(sum(change_values) / len(change_dict),2)

#Convert to a currency-friendly format
avg_change_currency = "${:,.2f}".format(avg_change)

#Find max/min month(key)/change(value) from the newly created dictionary (change_dict)
max_month = max(change_dict.keys(), key=(lambda k: change_dict[k]))
min_month = min(change_dict.keys(), key=(lambda k: change_dict[k]))
max_change = change_dict[max(change_dict, key=change_dict.get)]
min_change = change_dict[min(change_dict, key=change_dict.get)]

#Convert to a currency-friendly format
max_change_currency = "${:,.2f}".format(max_change)
min_change_currency = "${:,.2f}".format(min_change)

#---------------------------------
#Print analysis to terminal 
#---------------------------------
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: " + total_currency)
print("Average Change: " + str(avg_change_currency))
print("Greatest Increase in Profits: " + str(max_month) + " (" + str(max_change_currency) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + " (" + str(min_change_currency) + ")")

#---------------------------------
#Print analysis to text file
#---------------------------------
with open("analysis/financial_analysis.txt", "w") as text_file:
    print(f"Financial Analysis", file=text_file)
    print(f"----------------------------", file=text_file)
    print(f"Total Months: {total_months}", file=text_file)
    print(f"Total: {total_currency}", file=text_file)
    print(f"Average Change: {avg_change_currency}", file=text_file)
    print(f"Greatest Increase in Profits: {max_month} ({max_change_currency})", file=text_file)
    print(f"Greatest Decrease in Profits: {min_month} ({min_change_currency})", file=text_file)