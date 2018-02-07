# Part 1
import os
import csv

# List of raw data sheets
electiondata = ['1', '2']
title = "Election Results"

for results in electiondata:

    # Grab CSV
    rawresults = os.path.join('/Users/stephaniechanshomefolder/Desktop/python-challenge/PyPoll', 'election_data_' + results + '.csv')

    # Create new CSV
    newresults = os.path.join('allresultselection.csv')

    Voter_ID = []
    County = []
    Candidate = []

# open reader for each CSV file
    with open(rawresults, 'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        next(csvreader, None)
        
        # store each row, set variables  
        for row in csvreader:

            Voter_ID.append(row[0])
            County.append(row[1])
            Candidate.append(row[2])
    
cleanCSV = zip(Voter_ID, County, Candidate)        

with open(newresults, 'w', newline='') as csvfile:
    
    csvWriter = csv.writer(csvfile, delimiter=',')
    csvWriter.writerow(["Voter_ID", "County", "Candidate"])
    csvWriter.writerows(cleanCSV)
    
# text = "Election Results"
# txtfile = open('file path' , 'w'/'a')
# txtfile.write(text)
# txtfile.close()
with open('Election Results.txt', 'a') as f:
#     # for line in newresults:
#     #     f.write(line)
    c = "{:.2%}".format(int(Candidate.count("Correy"))/int(len(Voter_ID)))
    l = "{:.2%}".format(int(Candidate.count("Li"))/int(len(Voter_ID)))
    k = "{:.2%}".format(int(Candidate.count("Khan"))/int(len(Voter_ID)))
    o = "{:.2%}".format(int(Candidate.count("O'Tooley"))/int(len(Voter_ID)))

print(title)
print("-"*35)
print('Total Votes: ' + str(len(Voter_ID)))
print("-"*35)
print('Correy: ' + c + ' ' + '(' + str(Candidate.count("Correy")) + ')')
print('Li: ' + l + ' ' + '(' + str(Candidate.count("Li")) + ')')
print('Khan: ' + k + ' ' + '(' + str(Candidate.count("Khan")) + ')')
print("O'Tooley: " + o + ' ' + '(' + str(Candidate.count("O'Tooley")) + ')')

# candidatelist = []
# print(candidatelist,file=open("newpollingtxt","a"))
# print(candidatelist)