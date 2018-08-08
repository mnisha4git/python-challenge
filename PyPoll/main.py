# First we'll import the os module
import os
import csv
#import time
from datetime import date
from datetime import time
from datetime import datetime

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


Total   = 0.00
candidateList = []



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print("CSV Header: ", csv_header)

    #print(csvreader) 
    # Read each row of data after the header
    for row in csvreader:
        Total  += 1
        if row[2] not in candidateList:
            candidateList.append(row[2])





#for candidate in candidateList:
    #for row in csvreader 
       #if row[2] == candidate
         # num +=1
          # num  number of votes per candidate
          # percent num/len
          # save candidate num percent  hvote  candidate name as winner
  



    print("Number of Candidates: "+ str(len(candidateList)))
    print("Total Votes: "+str(Total))
