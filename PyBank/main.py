import csv

# Path to the CSV file
file_path = "Resources\\budget_data.csv"

# Initialize variables to store financial data
total_months = 0
total_profit_losses = 0
profit_losses = []
months = []
# Read the CSV file
with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip header row
        for row in csvreader:
            # Extract data from each row
            month = row[0]
            profit_loss = int(row[1])

            # Update total months and total profit/losses
            total_months += 1
            total_profit_losses += profit_loss

            # Store profit/losses and months separately
            profit_losses.append(profit_loss)
            months.append(month)

            # Calculate changes in profit/losses
            changes = [profit_losses[i + 1] - profit_losses[i] for i in range(len(profit_losses) - 1)]

# Calculate average change
average_change = sum(changes) / len(changes)

# Find greatest increase and decrease in profits
max_increase = max(changes)
max_decrease = min(changes)
max_increase_month = months[changes.index(max_increase) + 1]
max_decrease_month = months[changes.index(max_decrease) + 1]

# Print analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

# Export analysis to a text file
output_path = "financial_analysis.txt"
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")

    print("Analysis exported to financial_analysis.txt")

