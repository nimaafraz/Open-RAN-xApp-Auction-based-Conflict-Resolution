# This implementation will support multiple xApps with multiple conflicting parameters.

import pandas as pd
import numpy as np
import csv

# Define the filename
filename = "bids_data.csv"

# Initialize an empty dictionary to store bids data
bids_data = {}

# Read data from CSV
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    # Iterate over rows
    for row in reader:
        xapp, icp, desired_value, bid_amount = row
        desired_value = int(desired_value)
        bid_amount = int(bid_amount)
        # If xapp key doesn't exist, create it
        if xapp not in bids_data:
            bids_data[xapp] = {}
        # If icp key doesn't exist under xapp, create it
        if icp not in bids_data[xapp]:
            bids_data[xapp][icp] = []
        # Append the bid (desired value, bid amount) to the list of bids for the icp
        bids_data[xapp][icp].append((desired_value, bid_amount))

# print("Bids data read from CSV:")
# print(bids_data)
# # Mock data for bids. In a real scenario, this data would be provided in a structured format like a CSV.
# # bids_data = {
# #     'MLB': {'TXP': [(10, 50), (15, 30)], 'TTT': [(5, 20)]},
# #     'CCO': {'TXP': [(100, 70), (90, 40)], 'RET': [(10, 60)]},
# #     'ES': {'TXP': [(50, 80)]},
# #     'MRO': {'TXP': [(20, 30), (25, 50)], 'CIO': [(3, 40)]},
# # }
# # Here, we simulate the bidding process with a dictionary for demonstration purposes.
# bids_data = {
#     # Each xApp (like MLB, CCO, ES, MRO) is a key in the dictionary
#     'MLB': {
#         # For each xApp, there's a nested dictionary where each key is a parameter (ICP) like TXP, TTT
#         'TXP': [
#             # The value for each parameter key is a list of tuples
#             (10, 50),  # Each tuple represents a bid, where the first element is the desired value for the parameter
#                        # and the second element is the amount of the bid.
#             (15, 30),  # For example, here MLB is willing to bid 50 for TXP to be set to 10, and 30 for TXP to be 15
#         ],
#         'TTT': [
#             (5, 20),   # Another bid by MLB for a different parameter (TTT), bidding 20 for TTT to be set to 5
#         ]
#     },
#     'CCO': {
#         # Similar structure for CCO, bidding on different values for TXP and RET parameters
#         'TXP': [
#             (100, 70), # CCO bids 70 for TXP to be set to 100
#             (90, 40),  # and 40 for TXP to be 90
#         ],
#         'RET': [
#             (10, 60),  # CCO also bids on RET, offering 60 for it to be set to 10
#         ]
#     },
#     'ES': {
#         # ES makes a single bid for TXP
#         'TXP': [
#             (50, 80),  # Bidding 80 for TXP to be set to 50
#         ]
#     },
#     'MRO': {
#         # MRO bids on both TXP and CIO parameters
#         'TXP': [
#             (20, 30),  # Bidding 30 for TXP to be 20
#             (25, 50),  # and 50 for TXP to be 25
#         ],
#         'CIO': [
#             (3, 40),   # Bidding 40 for CIO to be set to 3
#         ]
#     },
# }

def resolve_conflicts_with_winner(bids_data):
    # Combine all bids for each parameter with xApp names
    combined_bids = {}
    for xapp, params_bids in bids_data.items():
        for param, values_bids in params_bids.items():
            if param not in combined_bids:
                combined_bids[param] = {}
            for value, bid in values_bids:
                combined_key = (value, xapp)  # Store value and xApp as combined key
                if combined_key not in combined_bids[param]:
                    combined_bids[param][combined_key] = 0
                combined_bids[param][combined_key] += bid
    
    # Resolve conflicts by selecting the highest bid for each parameter and identifying the winner
    final_values_and_winners = {}
    for param, values_bids in combined_bids.items():
        highest_bid_key = max(values_bids, key=values_bids.get)  # Highest bid key is (value, xApp)
        highest_bid_value, winning_xapp = highest_bid_key
        final_values_and_winners[param] = (winning_xapp, highest_bid_value, values_bids[highest_bid_key])
    
    return final_values_and_winners

# Resolve the conflicts based on the mock bids data and identify winners
auction_results_with_winners = resolve_conflicts_with_winner(bids_data)

# Display the auction results along with the name of the winning xApp and their winning bid
for param, details in auction_results_with_winners.items():
    winning_xapp, value, bid = details
    print(f"Parameter: {param}, Winning xApp: {winning_xapp}, Winning Value: {value}, Winning Bid: {bid}")

