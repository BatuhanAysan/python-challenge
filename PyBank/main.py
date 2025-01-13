# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)

file_to_load = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join(os.path.dirname(__file__), "analysis", "budget_analysis.txt")  # Output file path

# Open and read the csv
with open(file_to_load, 'r') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

# Define variables to track the financial data
    total_months = 0
    total = 0
    current_month_value = 0
    total_changes = 0
    changes = []
    previous_value = 0
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}

    # Process each row of data

    for row in reader:

        # Track the total months

        total_months += 1

        # Track the total

        current_month_value = int(row[1])
        total += current_month_value

        # Track the changes 

        if previous_value != 0:
            change = current_month_value - previous_value
            total_changes += change
            changes.append(change)

        # Calculate the greatest increase in profits (month and amount)

            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = row[0]

        # Calculate the greatest decrease in losses (month and amount)

            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = row[0]

        previous_value = current_month_value

# Calculate the average net change across the months

    average_change = total_changes / len(changes) if changes else 0

# Generate the output summary

print("Financial Analysis\n......................")

# Print the output
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Write the results to a text file

with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"......................\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

print(f"Analysis has been written to {file_to_output}")