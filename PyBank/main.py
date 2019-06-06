import csv

# Files load and output 
file_load = "budget_data.csv"
file_output = "analysis.txt"

# tracking the parameters
total_months = 0
total_amount = 0
previous = 0
month_change = []
profit_change_list = []
max_increase = 0 
max_decrease = 0

# read the csv & convert to dictionaries 
with open(file_load) as profit_data:
    reader = csv.reader(profit_data)

    next(reader)

    for row in reader:

        # track total
        total_months = total_months + 1 
        total_amount = total_amount + int(row[1])


        if total_months > 1:
            change = int(row[1])-previous
            month_change.append(change)

            if change > max_increase:
                max_increase = change 
                max_increase_month = row[0]

            if change < max_decrease:
                max_decrease = change
                max_decrease_month = row[0]

        previous = int(row[1])

# Calculate average profit change

average = round(sum(month_change)/(len(month_change)+ 0.0),2)

output = ('Financial Analysis'+ '\n'+
          '.........................'+ '\n'  +
          'Total Months: ' + str(total_months) + '\n' +
          'Total: ' + ' $'+ str(total_amount) + '\n' +
          'Average Change:' + ' $' + str(average) + '\n' +
          'The Greatest Increase in Profits: ' + max_increase_month + ' $' + str(max_increase) + '\n' +
          'The Greatest Decrease in Profits: ' + max_decrease_month + ' $' + str(max_decrease) + '\n')

      

print(output)

with open(file_output, 'w') as outputfile:
    outputfile.write(output)