# Importing this function to clear the screen.
from replit import clear

# Importing the logo from art.
from art import logo

# Printing the logo.
print(logo)

# Dictionary to store the key:value pairs.
bids = {}

# Flag that controls while loop.
bidding_finished = False

# Function that chooses the highest_bidder from the inputed data.
def find_highest_bidder(bidding_record):
  
  highest_bid = 0
  winner = ""
  
  # To loop through each item in the dictionary and to find the highest_bid.
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder

  # Printing results.  
  print(f"The winner is {winner} with a bid of ${highest_bid}")

# To run the code indefinetly.
while not bidding_finished:

  # Getting input from the user.
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

  # Contining based on user input.
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    # Clear screen.
    clear()
  
  
# https://replit.com/@TharunReddy5/BlindAuction#main.py