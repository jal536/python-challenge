#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
budget_data


# In[ ]:


date_id = []
profit_id = []


# In[ ]:


with open(budget_data, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    header = next(csvreader)
    print(f"CSV Header: {header}")
        
    # Read each row of data after the header
#The total number of months included in the dataset
    months = 0
    for row in csvreader:
        date_id.append(row[0])
        profit_id.append(row[1])
        months += 1
       # print(months)


# In[ ]:


#The net total amount of "Profit/Losses" over the entire period
totalprofit = 0
for i in profit_id:
    totalprofit += int(i)
    #print(i)


# In[ ]:


#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

max_inc = 0
max_dec = 0
inc_date = ""
dec_date = ""

changeTotal = 0

for i in range(len(profit_id) - 1):
    changeValue = int(profit_id[i+1]) - int(profit_id[i])
    changeTotal += changeValue
    if (changeValue > 0):
        if changeValue > max_inc:
            max_inc = changeValue
            inc_date = date_id[i+1]
    else:
        if changeValue < max_dec:
            max_dec = changeValue
            dec_date = date_id[i+1]
    #print(changeValue)

#print("increase: ", max_inc, inc_date)
#print("decrease: ", max_dec, dec_date)


# In[ ]:


print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total Profit/Losses: " + "$" + str(round(totalprofit, 2)))
print("Average Change: " + "$" + str(round(changeTotal/(months - 1), 2)))
print("Greatest Increase in Profits: " + inc_date + " ($" + str(max_inc) + ")")
print("Greatest Decrease in Profits: " + dec_date + " ($" + str(max_dec) + ")")


# In[ ]:


# Create the path for the filename
Financial_analysis = os.path.join("Resources", "Financial Analysis.csv")

# Write data to a .csv file
with open(Financial_analysis, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # To save specific data input as a row in the csv
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Months: " + str(months)])
    writer.writerow(["Total Profit/Losses: " + "$" + str(round(totalprofit, 2))])
    writer.writerow(["Average Change: " + "$" + str(round(changeTotal/(months - 1), 2))])
    writer.writerow(["Greatest Increase in Profits: " + inc_date + " ($" + str(max_inc) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + dec_date + " ($" + str(max_dec) + ")"])


# In[ ]:




