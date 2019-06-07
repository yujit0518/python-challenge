import csv

# Load the csv file and write code for output results
file_load = "budget_data.csv"
file_output = "Bank_Analysis.txt"

# tracking the parameters and creating variables from existing data
total_months = 0
total_amount = 0
previous = 0
month_change = []
profit_change = []
greatest_increase = 0 
greatest_decrease = 0

# read the cvs files
with open(file_load) as profit_data:
    reader = csv.reader(profit_data)
    next(reader)
    for row in reader:

        # track total amount/months
        total_months = total_months + 1 
        total_amount = total_amount + int(row[1])

        if total_months > 1:
            change = int(row[1])-previous
            month_change.append(change)
            if change > greatest_increase:
                greatest_increase = change 
                max_increase_month = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                max_decrease_month = row[0]
        previous = int(row[1])

# Calculate the resullt and changes
average = round(sum(month_change)/(len(month_change)+ 0.0),2)

output = ('Financial Analysis'+ '\n'+
          '.........................'+ '\n'  +
          'Total Months: ' + str(total_months) + '\n' +
          'Total: ' + ' $'+ str(total_amount) + '\n' +
          'Average Change:' + ' $' + str(average) + '\n' +
          'Greatest Increase in Profits: ' + max_increase_month + ' $' + str(greatest_increase) + '\n' +
          'Greatest Decrease in Losses: ' + max_decrease_month + ' $' + str(greatest_decrease) + '\n')

print(output)
with open(file_output, 'w') as outputfile:
    outputfile.write(output)