#Allows file path to be opened in differing OS
import os 

#Module that allow CSV to be read 
import csv

#Setting path to csv file 
csvpath = os.path.join('Resources', 'budget_data.csv')

#Initializing total months variable 
total_months = 0

#Initializing Profit List
profits = []

#Initializing Net Profit Variable
net_profit = 0

#Intializing monthly change variables
monthly_change = 0

#Initalizing monthly profit change list
monthy_change_list = []

#Initalizing a date/month list
date = []

#Telling program to read csv
with open(csvpath) as csvfile:

    # CSV reader read files with comma dictating seperate columns 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Reads the header rown first 
    csv_header = next(csvreader)

    #Print Financial Analyiss 
    print("Financial Analysis")

    print("-------------------")

    #For loop goes through every row in the csv
    for row in csvreader:
        #count the number of rows in the row to determine total number opf months since we have clean non-repetitive data
        total_months+=1
        #Takes all the profit values in the csv file and adds it to the profits list initalized earlier  
        profits.append(row[1])
        #Appends all the dates to date list iniitalized earlier 
        date.append(row[0])

    #Loops through the profits list based on the length of the list 
    for i in range(len(profits)): 
        #adds the values in list by looping through each index to determine net profit 
        net_profit += int(profits[i])
        #If statement make sure program only runs if within the lnegth of the profits list to prevent program error
        if int(i+1) < len(profits):
            #calcuale the change in profit month to month 
            change = (int(profits[i+1])) - (int(profits[i]))
            #Appending list of changes to a list called monthly changes 
            monthy_change_list.append(change)
            #Sum up the change in profit month to month 
            monthly_change += change
    #Calculating the average change and using round function to round answer to 2 decimal places 
    average_change = round((monthly_change)/(total_months-1), 2)

    #Loops through the profits chane list based on the length of the list 
    for i in range(len(monthy_change_list)): 
        #Determines the index value/month where the greatest increase in profit occured
        if monthy_change_list[i] == max(monthy_change_list):
            Max_Bingo = i+1
        #Determines the index value/month where the greatest decrease in profit occured
        elif monthy_change_list[i] == min(monthy_change_list):
            Min_bingo = i+1

    #Prints the total number of months included in the dataset
    print(f"Total months: {total_months}")
    #Prints the net total amount of "Profit/Losses" over the entire period
    print(f"Total: {net_profit}")
    #Prints the Average profit/loss change 
    print(f"Average Change: {average_change}")
    #The greatest increase in profits (date and amount) over the entire period
    print(f"Greatest Increase in Profits: {date[Max_Bingo]} ({max(monthy_change_list)})")
    #The greatest decrease in profits (date and amount) over the entire period
    print(f"Greatest Decrease in Profits: {date[Min_bingo]} ({min(monthy_change_list)})")

#Setting output file path
file_output_path = os.path.join('Analysis', 'budget_analysis.txt')

#Output Summary 
output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total months: {total_months}\n"
    f"Total: {net_profit}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {date[Max_Bingo]} ({max(monthy_change_list)})\n"
    f"Greatest Decrease in Profits: {date[Min_bingo]} ({min(monthy_change_list)})\n"
    )
     
#Export text file 
with open(file_output_path, "w") as txt_file:
    txt_file.write(output)
