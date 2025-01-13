# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join(os.path.dirname(__file__), "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates =[]
name_vote = {}
# Winning Candidate and Winning Count Tracker
percentage_votes = 0
winning_candidate = None
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidates_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidates_name not in candidates:
            candidates.append(candidates_name)
        
        # Add a vote to the candidate's count
            name_vote[candidates_name] = 1
        else:
            name_vote[candidates_name] += 1
    
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("\nElection Results\n........................")
    print(f"Total Votes: {total_votes}")
    # Write the total vote count to the text file
    txt_file.write(f"Election Results\n........................\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("........................\n")
    print("........................")
    # Loop through the candidates to determine vote percentages and identify the winner
    for key, value in name_vote.items():

        # Get the vote count and calculate the percentage
        perc_vote = (value / total_votes) * 100
        
        # Update the winning candidate if this one has more votes
        if perc_vote > percentage_votes:
            winning_candidate = key
            percentage_votes = perc_vote

        # Print and save each candidate's vote count and percentage
        
        print(f"{key}: {perc_vote:.3f}% ({value})")
        txt_file.write(f"{key}: {perc_vote:.3f}% ({value})\n")
    print("........................")
    txt_file.write("........................\n")

    # Generate and print the winning candidate summary
    print(f"Winner: {winning_candidate}")
    print("........................")

    # Save the winning candidate summary to the text file
    txt_file.write(f'Winner: {winning_candidate}\n')
    txt_file.write("........................")