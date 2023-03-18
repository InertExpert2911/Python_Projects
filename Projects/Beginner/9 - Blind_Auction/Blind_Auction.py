# Module to clear screen
import os

# Import ASCII art logo
# from auction_art import logo
# print(logo)


def store_user_details(name, bid):
    user_details = {}
    user_details["name"] = name
    user_details["bid"] = bid

    auctioneers.update(user_details)

# def auction_winner(auctioneers):

#     highest_bid = 0

#     for bid in auctioneers["bid"]:

#         # Check the bid they placed and update highest bid
#         print(bid)


auctioneers = {}

# control_loop = True

# while control_loop:

user_name = input("What is your name?: ")
bid_amount = input("What is your bid?: $ ")

are_there_other_users = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

if are_there_other_users == 'yes':
    # To clear the screen
    # os.system('cls')
    print("clear")
    user_name = input("What is your name?: ")
    bid_amount = input("What is your bid?: $ ")
elif are_there_other_users == 'no':
    #auction_winner(auctioneers)
    print(f"The winner is with a bid of $")
    #control_loop = False

store_user_details(user_name, bid_amount)
print(auctioneers)
