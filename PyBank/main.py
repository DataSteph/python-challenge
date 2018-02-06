# Part 1
import os
import csv
# csvpath1 = "/Users/stephaniechanshomefolder/desktop/UCB_Data-Homework/Homework3-Python/PyBank/budget_data_1.csv"

# List of raw budget data sheets
budgetdata = ['1', '2']
title = "Financial Analysis"
looper = 0 
look_up_value = 0
# Loop through years
for budget in budgetdata:

    # Grab wrestling CSV
    ogbudgetdata = os.path.join('/Users/stephaniechanshomefolder/desktop/UCB_Data-Homework/Homework3-Python/PyBank/', 'budget_data_' + budget + '.csv')

    # Create new CSV
    newbudgetdata = os.path.join('newbudget.csv')

    months = []
    revenues = []
    total = 0

# open reader for each CSV file
    with open(ogbudgetdata, 'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        next(csvreader, None)
        
        # store each row, set variables  
        for row in csvreader:

            months.append(row[0])
            revenues.append(int(row[1]))
    
cleanCSV = zip(months, revenues)        
            
with open(newbudgetdata, 'w', newline='') as csvfile:
    
    csvWriter = csv.writer(csvfile, delimiter=',')
    csvWriter.writerow(["Months", "Revenues"])
    csvWriter.writerows(cleanCSV)

print(title)
print("-"*35)
# Calculate the total number of months included in the dataset
print('Total months: ' + str(len(months)))

# Calculate the total amount of revenue gained over the entire period
for r in revenues:
    total += r
print('Total revenue: $' + str(total))

# The average change in revenue between months over the entire period
i = 0
dif = []
while i < len(revenues)-1:
    dif.append((revenues[i + 1]) - (revenues[i]))
    i = i + 1
print('Average Revenue Change: $' + str((sum(dif))/(len(dif)))

# #  The greatest increase in revenue (date and amount) over the entire period
# # This value is to keep track of where I am in the dif list as in loops through to find the max
# This value is to be used to look up corresponding month in the months list
looper = 0
look_up_value = 0
for n in dif # Loop through the dif list 
    if max(dif) == n # if the max of the dif list is equal to the current value for n in the loop
        look_up_value = looper # make the look_up_value equal to the current interation of the loop
    else
        looper += 1 # else, keep going, making sure that the placeholder I'm at is also increasing
print('Greatest Increase in Revenue: ' + months[look_up_value + 1] + ' $' + str(max(dif)))

# # The greatest decrease in revenue (date and amount) over the entire period
looper = 0
look_up_value = 0
for n in dif:
    if min(dif) == n:
        look_up_value = looper
    else:
        looper += 1
print('Greatest Decrease in Revenue: ' + months[look_up_value + 1] + ' $' + str(min(dif)))