# First we'll import the os module
import os
import csv
import calendar
import locale 
import sys
from datetime import datetime

csvpath = os.path.join('..', 'Resources', 'budget_data_test.csv')

filename  = open("outputfile.txt",'w')
sys.stdout = filename
Total    = 0.00
counter  = 0
monthly_revenue  =  0.00
average_change   =  0.00

monthList = []
prev_record    = {"month": "01-1900","rev_amt": 0.00} 
oldest_rec     = {"month": "01-1900","rev_amt": 0.00 }
latest_rec     = {"month": "01-1900","rev_amt": 0.00 }
highest_profit = {"month": "01-1900","rev_amt": 0.00 }
lowest_profit  = {"month": "01-1900","rev_amt": 0.00 }

#print(locale.getlocale())
locale.setlocale(locale.LC_ALL, '')
#print(locale.nl_langinfo(locale.D_FMT))




with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        #print(row[0]+ ":" +row[1])
        date1 = datetime.strptime (row[0],"%m/%d/%y")
        month = str(date1.month)+"-"+ str(date1.year)
        #print(prev_record["month"]+" : "+month)
        if highest_profit["rev_amt"] < float(row[1]):
            highest_profit = {"month": month,"rev_amt": float(row[1])}
        if lowest_profit["rev_amt"] > float(row[1]):
            lowest_profit = {"month": month,"rev_amt": float(row[1])}

        if prev_record["month"]!= month:
                if counter >0:
                   Total  = Total + prev_record["rev_amt"] 
                   monthly_revenue =  monthly_revenue + prev_record["rev_amt"] 
                   average_change  =  latest_rec["rev_amt"]-oldest_rec["rev_amt"]
                   #print(prev_record["month"]+" : "+month+" : "+ str(monthly_revenue) +" : "+ str(average_change))
                   monthList.append({"month":prev_record["month"],"rev_amt":monthly_revenue,"diff":average_change})
                average_change   = 0.00
                monthly_revenue  = 0.00
                oldest_rec = {"month": month,"rev_amt":float(row[1])}
                latest_rec = {"month": month,"rev_amt":float(row[1])}
        else:
                Total  = Total + prev_record["rev_amt"]
                monthly_revenue =  monthly_revenue + prev_record["rev_amt"] 
                latest_rec = {"month": month,"rev_amt":float(row[1])}
                #print(prev_record["month"]+" : "+month+" : "+ str(monthly_revenue) +" : "+ str(average_change))
                

        prev_record =    {"month": month,"rev_amt":float(row[1])}
        counter = counter +1 
   
    Total  = Total + prev_record["rev_amt"]    
    monthly_revenue =  monthly_revenue + prev_record["rev_amt"] 
    average_change  =  latest_rec["rev_amt"]-oldest_rec["rev_amt"]
    monthList.append({"month":month,"rev_amt":monthly_revenue,"diff":average_change})

    average_change = 0.00  
    for row in monthList:
        #print(row["month"]+" : "+str(row["rev_amt"])+" : "+str(row["diff"]))
        average_change = average_change + float(row["diff"])

   
    print("Financial Analysis")
    print("-------------------------------------------------------------------")     

    print("Total Months: "+ str(len(monthList)))
    print("Total: "+str(Total))
    print("Average Change : "+ str(average_change/(len(monthList)-1)))
    print("Greatest Increase in Profits: "+"  "+highest_profit["month"]+" ($"+ str(highest_profit["rev_amt"])+")")
    print("Greatest Decrease in Profits: "+"  "+lowest_profit["month"] +" ($"+ str(lowest_profit["rev_amt"])+")")

    print("-------------------------------------------------------------------")

