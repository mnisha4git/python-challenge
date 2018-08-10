# First we'll import the os module
import os
import csv
#import time
from datetime import date
from datetime import time
from datetime import datetime

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

Total = 0.00
monthList = []
lrev_amt  = -9999.99
hrev_amt  =  0.00
lrev_day  = '01/01/1900'
hrev_day  = '01/01/1900'

month_detail = {
                      "name": "01-JAN",
                      "least_rev": 0.00,
                      "lrev_day": "01/01/2000",
                      "high_rev": 0.00,
                      "hrev_day": "01/01/2000",
                      "diff": 0.00 ,
                      "diff_percent":0.00 }



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print("CSV Header: ", csv_header)

    #print(csvreader) 
    # Read each row of data after the header
    for row in csvreader:
        Total  = Total+ int(row[1])

        date1 = datetime.strptime (row[0],"%m/%d/%y") 
        date2= str(date1.month)+"-"+ str(date1.year)

        if str(date2) not in monthList:
           monthList.append(str(date2))

        for month in monthList:
            if date2 ==month:
                #print(month)  
                if float(row[1]) < float(lrev_amt):
                    lrev_amt = row[1]
                    lrev_day = row[0]
                   
                if float(row[1]) > float(hrev_amt):
                    hrev_amt = row[1]
                    hrev_day = row[0]

                month_detail = {
                      "name": month,
                      "lrev_amt": lrev_amt,
                      "lrev_day": lrev_day,
                      "hrev_amt": hrev_amt,
                      "hrev_day": hrev_day,
                      "diff":  float(hrev_amt)-float(lrev_amt) ,
                      "diff_percent": ((float(hrev_amt)-float(lrev_amt))/Total) }
            #print(month_detail["name"] +  ":" + month_detail["lrev_amt"][0])  

    print("-------------------------------------------------------------------")
    for key, value in month_detail.items():
            #print(f"This is a key (again): {key}")
            #print(f"This is a Value (again): {value}")  
            print(f"Greatest increase in profits:  {month} ({hrev_amt})")
            print(f"Greatest increase in profits:  {month} ({lrev_amt})")      

    print("Total Months: "+ str(len(monthList)))
    print("Total: "+str(Total))

    print("-------------------------------------------------------------------")
