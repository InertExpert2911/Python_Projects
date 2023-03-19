# Module to clear screen
import os

# Import ASCII art logo and print it
from auction_art import logo
print(logo)

# Function to append user details as a dictionary to the list auction_details
def add_auction_details(name, bid):
    
    # A temp dictionary to store user name and bid amount
    temp_auction_details = {}
    
    # Adding key:value pairs to the above dictionary
    temp_auction_details["name"] = name
    temp_auction_details["bid"] = bid
    
    # Append the new user details to the list auction_details
    auction_details.append(temp_auction_details)
    
# Function to get the highest bid amount from all the bids placed
def get_highest_bid(auction__user_details):
    
    # Empty variables to store highest bid and the user with highest bid
    highest_bid = 0
    get_user = ""
    
    # loops through each dictionary in the list auction_details
    for user in auction_details:
        
        # If user's bid amount which is an int() > highest bid variable value, update the variable
        if user["bid"] > highest_bid:
            highest_bid = user["bid"]
            # print(highest_bid)
            
            # Get user name
            get_user = user["name"]
            
    # Print result
    print(f"The winner is {get_user} with a bid amount of {highest_bid}")
    
# Control the while loop
while_bidding_complete = False

# While loop
while not while_bidding_complete:
    
    # Inputs from the user
    user_name = input("What is your name?: ")
    # Convert to int to find highest bid
    bid_amount = int(input("What is your bid?: $ ")) 
    are_there_other_users = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    # List to store user name and bid
    auction_details = []
    
    # Call the function to add details in the above list
    add_auction_details(user_name, bid_amount)
    # print(auction_details)
    
    # Run till the user input is yes
    while are_there_other_users == 'yes':

        # To clear the screen
        os.system('cls')
        
        # WASTE CODE
        user_name = input("What is your name?: ")
        bid_amount = int(input("What is your bid?: $ "))
        are_there_other_users = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
        add_auction_details(user_name, bid_amount)
        # print(auction_details)
    
    # If user's choice is 'no', then get the highest bid and end the while loop
    if are_there_other_users == 'no':
        get_highest_bid(auction_details)
        while_bidding_complete = True
    
    # print(auction_details)
    
    
    
    


