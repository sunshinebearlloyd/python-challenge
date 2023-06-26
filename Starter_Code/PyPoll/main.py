# Dependencies
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#Print Header for results
print("\nElection Results\n\n--------------------------\n")

count = 0
Stockham = 0
DeGette = 0
Doane = 0
win_vote = ' '

#open csvpath as csvfile:
with open(csvpath) as csvfile:
    #call csv.reader function to read file specifying the delimiter and the variable to hold the content
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first and stores it per instructions
    csv_header = next(csvreader)

    # Read each row of data after the header and save to list variables
    for row in csvreader:

        #count number of ballots by counting number of rows
        count = count + 1

        #Count votes based on who the chosen candidate is on the ballot
        if (row[2] == "Charles Casper Stockham"):
            Stockham = Stockham + 1
        elif (row[2] == 'Diana DeGette'):
            DeGette = DeGette + 1
        elif(row[2] == 'Raymon Anthony Doane'):
            Doane = Doane + 1
        else:
            print('unexpexcted vote')

    #Calculate percentages
    Stockham_percentage = round(((Stockham/count)*100),3)
    DeGette_percentage = round(((DeGette/count)*100), 3)
    Doane_percentage = round(((Doane/count)*100), 3)

    
    #Compare the votes per candidate to the max votes per candidate
    #  if they match then they are the winning vote 
    if (Stockham == max(Stockham, DeGette, Doane)):
        win_vote = "Charles Casper Stockham"
    elif(DeGette == max(Stockham, DeGette, Doane)):
        win_vote = 'Diana DeGette'
    else:
        win_vote = 'Raymon Anthony Doane'
     

    #Print results to terminal    
    print(f'Total Votes:  {count}\n\n--------------------------\n')
    print(f'Charles Casper Stockham: {Stockham_percentage}% ({Stockham})\n')
    print(f'Diana DeGette: {DeGette_percentage}% ({DeGette})\n')
    print(f'Raymon Anthony Doane: {Doane_percentage}% ({Doane})\n')
    print('--------------------------\n')
    print(f'Winner: {win_vote}\n\n--------------------------\n')

     
    
#Specify the file to write to
output_file = os.path.join("analysis", "results.txt")

# Open the file using "write" mode.
with open(output_file, "w") as f:
    
    #Write to output_file
    f.write("\nElection Results\n\n--------------------------\n\n")
    f.write('Total Total Votes: ' +str(count)+'\n\n--------------------------\n\n')
    f.write('Charles Casper Stockham: '+str(Stockham_percentage)+'% ('+str(Stockham)+')\n\n')
    f.write('Diana DeGette: '+str(DeGette_percentage)+'% ('+str(DeGette)+')\n\n')
    f.write('Charles Casper Stockham: '+str(Doane_percentage)+'% ('+str(Doane)+')\n\n--------------------------\n\n')
    f.write('Winner:  '+win_vote+'\n\n--------------------------\n\n')
f.close()


