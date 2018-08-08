# First we'll import the os module
import os
import csv
#import time
from datetime import date
from datetime import time
from datetime import datetime

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


counter = 0
Total   = 0.00
date1   = '1/13/2018'
date2   = '1/13/2018'
monthList = []
least_rev =999999999.00
high_rev =0.00
lrev_day = '01/01/2000'
hrev_day = '01/01/2000'


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print("CSV Header: ", csv_header)

    #print(csvreader) 
    # Read each row of data after the header
    for row in csvreader:
        Total  += int(row[1])
        date1 = datetime.strptime (row[0],"%m/%d/%y") 
        date2= str(date1.month)+"-"+ str(date1.year)
        #print(date2)

        if date2 not in monthList:
            monthList.append(date2)


    month_detail = {
                      "name": "01-JAN",
                      "least_rev": 0.00,
                      "lrev_day": "01/01/2000",
                      "high_rev": 0.00,
                      "hrev_day": "01/01/2000",
                      "diff": 0.00 ,
                      "diff_percent":0.00 }

    for month in monthList:
        print("1")
        for row in csvreader:
            print("2")
            date1 = datetime.strptime (row[0],"%m/%d/%y") 
            date2= str(date1.month)+"-"+ str(date1.year)
            print(str(date2))
            print(str(row[0]) +":" +str(row[1]) )
            if date2 == month:
                if row[1] < least_rev:
                    least_rev = row[1]
                    lrev_day = row[0]
                   
                if row[1] > high_rev:
                    high_rev = row[1]
                    hrev_day = row[0]

        month_detail = {
                      "name": month,
                      "least_rev": least_rev,
                      "lrev_day": lrev_day,
                      "high_rev": high_rev,
                      "hrev_day": hrev_day,
                      "diff":  high_rev-least_rev ,
                      "diff_percent": ((high_rev-least_rev)/Total) }
        print(f'{month_detail["name"]}  {month_detail["least_rev"]}  {month_detail["high_rev"]}')

            


    print("Total Months: "+ str(len(monthList)))
    print("Total: "+str(Total))
