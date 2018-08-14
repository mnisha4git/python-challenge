# First we'll import the os module
import os
import csv
import sys
import operator

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
filename  = open("output_file.txt",'w')
sys.stdout = filename

Total   = 0.00
candidateList = []
candidate = ' '
counter =0
num_votes = 0
prev_record    = {"voter_id":0,"name": ' '} 
winner_record    = {"name": ' ',"num_votes":0} 
winner_count = 0

data = csv.reader(open(csvpath),delimiter=',')
# 2 specifies according to third column we want to sort
sortedlist = sorted(data, key=operator.itemgetter(2))    
#now write the sorte result into new CSV file
with open("NewFile.csv", "w") as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
              fileWriter.writerow(row)


with open("NewFile.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        Total = Total+1 
        if prev_record["name"]!= str(row[2]):
            if Total > 1:
               candidateList.append({"name":prev_record["name"],"num_votes":num_votes})
               num_votes = 0
            prev_record =    {"voter_id":row[0],"name":row[2]} 
            num_votes = num_votes +1 
        else:
           num_votes = num_votes +1
           prev_record =    {"voter_id":row[0],"name":row[2]}  

candidateList.append({"name":prev_record["name"],"num_votes":num_votes})
prev_record =    {"voter_id":row[0],"name":row[2]}  
         


print("Election Results")
print("------------------------------------------------------")
print("Total Votes: "+str(Total))
print("------------------------------------------------------")
for candidate in candidateList:
    vote_percent = round((candidate["num_votes"]/Total)*100,3)
    print(candidate["name"]+ ": " + str(vote_percent) + "% (" +str(candidate["num_votes"])+ ")" )
    if int(winner_record["num_votes"]) < int(candidate["num_votes"]):
       winner_record = {"name":candidate["name"],"num_votes":int(candidate["num_votes"])} 
print("------------------------------------------------------")
print("Winner: "+winner_record["name"])
print("------------------------------------------------------")

