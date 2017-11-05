

# homework 1 , paybank


import csv

import string

Total_months = 0 #set initial value for month
H_increase={} #create an empty dictionary for high increase
H_decrease={} #create an empty dictionary for high decrease

Total_revenue = 0 #set initial value for revenue
max_change=0 
min_change=0
counter=0

files =["budget_data_1.csv", "budget_data_2.csv"]

for file in files:


    with open(file,newline="") as csvfile:


        csvreader =csv.reader(csvfile)

        next(csvreader,None) #skip header

       


        for x in csvreader:
            if x[1].isdigit():
                
                

                Total_revenue+=int(x[1])
                Total_months+=1
                
                
                # set counter to set initial value to calculate changes
                # i couldn't find formula to compare row1 to row2 in csv 
                if counter < 1:
                    counter =1
                    changes=int(x[1])

                elif counter < 2:
                    counter = 2
                    max_change= changes - int(x[1]) # now we have first changes
                    min_changes=changes - int(x[1]) # we set this one for min changes
                    changes=int(x[1])
                else:
                    
                    # we compare new row with previous row and the we reset change to the latest value in X[1]
                
                    changes = changes -int(x[1]) 


                    if changes > max_change:
                        H_increase[x[0]]=changes #add to dictionart high increase
                        # reset value change to the latest value in X[1] to calculate new change
                        changes=int(x[1]) 
                    
                    elif changes < min_change:
                        H_decrease[x[0]]=changes#add to dictionary high decrease
                        # reset value change to the latest value in X[1] to calculate new change
                        changes=int(x[1]) 

    # now we have 2 dictionaries for high increase and decrease
    # set it to zero to find the greatest change in
    # loop through dictionary to find the highest and month
    max_increase=0 
    for key,value in H_increase.items():
        if value > max_increase:
            max_increase = value
            month_value_high = key

    # set it to max to find the greatest decrease 
    # loop through dictionary to find the lowest and month
    max_decrease =max_increase
    for key,value in H_decrease.items():
        
        if value < max_decrease:
            
            max_decrease = value
            month_value_low= key
      
    Average_revenue= round((Total_revenue)/(Total_months),2)  

    print ("\n")
    
    print("Financial Analysis for "+str(file))

    print("-----------------------------------------------")        
    print ("Total Months : %s " %(Total_months))
    print ("Total Revenue is: $%s" %Total_revenue )
    print ("Average Revenue is: $%s"  %Average_revenue)
    print("Greatest Increase in Revenue: %s  $%s" %(month_value_high, max_increase))
    print("Greatest Decrease in Revenue: %s  $%s" %(month_value_low,max_decrease))

    print("-----------------------------------------------")
    print ("\n")


 
