

# homework 1 , paybank


import csv

import string

Total_months = 0
Average_changes=0
Total_revenue = 0
files =["budget_data_1.csv", "budget_data_2.csv"]

for file in files:


    with open(file,newline="") as csvfile:


        csvreader =csv.reader(csvfile)

        next(csvreader,None) #skip header

       


        for x in csvreader:
            if x[1].isdigit():
                Total_revenue+=int(x[1])
                Total_months+=1
                Average_changes
    
           
    print ("\n")
    
    print("Financial Analysis for "+str(file))

    print("------------------------")        
    print (Total_months)
    print(Total_revenue)
    print ("Total Months is: %s " %(Total_months))
    print ("Total Revenue is: $%s" %Total_revenue )
    Average_revenue= round((Total_revenue)/(Total_months),2)
    print ("Average Revenue is: $%s"  %Average_revenue)
    # # Greatest Increase in Revenue: Sep-16 ($815531)
    # # Greatest Decrease in Revenue: Aug-12 ($-652794)

    print("------------------------")
    print ("\n")


 
# # Greatest Increase in Revenue: Sep-16 ($815531)
# # Greatest Decrease in Revenue: Aug-12 ($-652794)


# ```
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
# ```