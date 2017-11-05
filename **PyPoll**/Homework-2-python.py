

# Homework 2 -Python , Pypol

# note : there is only one csv file for election


import csv
import string

winner={}
votes=0 # initial value for find the winner 


# csv file and code are in the same folder 

with open("election_data_2.csv", newline="") as raw_file:

    
    pol= csv.reader(raw_file, delimiter=',')

    #pol= next(pol) this doesn't work here

    candidate={} # dictionary for candidates

    total_votes=0
    
    for line in pol:
        total_votes+=1
        
        if line[2] not in candidate:
          
            candidate[line[2]]= 1

        else:
            candidate[line[2]]= candidate[line[2]]+1  # adding vote for each candidate              
   
        
print ("\n")  # empty line 
print("  Election Results ")
print("------------------------")
print ("Total Vote is: %s" %total_votes)
print("------------------------")

print ("Candidates:")

 
for key, value in candidate.items():
    percent_per_candidate=round((value / total_votes )*100,2)

    if value > 1 :
        print (key+":"+" " +str(percent_per_candidate)+"%" +" ", value )
    

        if  value > votes :
        
            votes=value
            winner[key]=votes   
    
print("------------------------")
for key, value in winner.items():
    print ("winner:",key, value)
    
    #print("Winner:%s" %Winner)
print("------------------------")
print ("\n")
