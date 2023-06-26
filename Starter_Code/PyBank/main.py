# Dependencies
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
date = []
profit_loss = []
change = []

#Print Header for results
print("\nFinancial Analysis\n--------------------------\n")


#open csvpath as csvfile:
with open(csvpath) as csvfile:
    #call csv.reader function to read file specifying the delimiter and the variable to hold the content
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first and stores it per instructions
    csv_header = next(csvreader)

    # Read each row of data after the header and save to list variables
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add profit_loss
        profit_loss.append(int(row[1]))

    #Find total months
    total_months = len(date)
    print(f'Total Months: {total_months}\n')

    #Calcualte total sum of profits and losses
    total_sum = sum(profit_loss)
    print(f'Total:  ${total_sum}\n')

    
    # Calculating monthly change in profits and losses and add to new list change
    for x, y in zip(profit_loss[0::], profit_loss[1::]):
        change.append(int(y-x))
        
    #Calculate the everage change in profits and losses:
    # sum of changes divded by the numer of elements in changes list
    # which should be one less than pofit_loss list
    avg_change = round((sum(change)/len(change)), 2)
    print(f'Average Change: $  {avg_change} \n')
    
    #Calculate the greatest increase in profits
    greatest_increase = max(change)

    #Get and format date for greatest increase in profits
    greatest_increase_date = date[change.index(greatest_increase) +1]
    
    #print date of greatest increase and it's vsalue
    print(f'Greatest Increase in Profits:  {greatest_increase_date}  (${greatest_increase})\n')

    #Calculate the greatest decrease in profits
    greatest_decrease = min(change)
    
    #Get and format date for greatest decrease in profits
    greatest_decrease_date = date[change.index(greatest_decrease) +1]

    #print date of greatest decrease and it's value
    print(f'Greatest Increase in Profits:  {greatest_decrease_date}  (${greatest_decrease})\n')
    
#Specify the file to write to
output_file = os.path.join("analysis", "test.txt")

# Open the file using "write" mode.
with open(output_file, "w") as f:
    
    #Write to output_file
    f.write("\nFinancial Analysis\n\n--------------------------\n\n")
    f.write('Total Months:' +str(total_months)+'\n\n')
    f.write('Total:  $'+str(total_sum)+'\n\n')
    f.write('Average Change: $  '+str(avg_change)+' \n\n')
    f.write('Greatest Increase in Profits:  '+greatest_increase_date+'  ($'+str(greatest_increase)+')\n\n')
    f.write('Greatest Increase in Profits:  '+greatest_decrease_date+'  ($'+str(greatest_decrease)+')\n\n')
f.close()


