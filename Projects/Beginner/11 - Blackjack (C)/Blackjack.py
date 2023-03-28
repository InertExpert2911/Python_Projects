# A game of Blackjack

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random

# user_hand = []
# dealer_hand = []

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# sample() method returns a list with a randomly selection of a specified number of items from a sequence.
# This method does not change the original sequence.

# Eg: Return a list that contains any 2 of the items from a list:
# import random
# my_list = ["apple", "banana", "cherry"]
# print(random.sample(my_list, k=2))


# user_hand += random.sample(cards, 2)
# dealer_hand += random.sample(cards, 2)

# print(user_hand)
# print(dealer_hand)

# user_score = sum(user_hand)
# dealer_score = sum(dealer_hand)

# print(user_score)
# print(dealer_score)

# if user_score == 21:
#     print("User wins the round!")
# elif dealer_score == 21:
#     print("The dealer wins this round, you lost.")
# else:
#     if user_score > 21:
#         if 11 in user_hand:
#             print("User has ACE")
#             # TODO: IF ace counts as a 1 instead of 11 are they still over 21?
            
#         else:
#             print("You lost")



# Function that uses the List below to *return* a random card.
# 11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


user_cards = []
computer_cards = []

# Deal the user and computer 2 cards each using deal_card() and append().

user_cards.append(deal_card())
user_cards.append(deal_card())

computer_cards.append(deal_card())
computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)

# Hint 6: Create a function called calculate_score() that takes a list of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

def calculate_score(list_of_cards):
    
    score = sum(list_of_cards)
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
    if score == 21:
        # 0 will represent a blackjack in our game.
        return 0
    
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in list_of_cards and score > 21:
        
        list_of_cards.remove(11)
        list_of_cards.append(1)
        
        # Another way can be to get the index and replace the item at that specific index
        # index_of_ace = list_of_cards.index(11)
        # list_of_cards[index_of_ace] = 1
    
    return sum(list_of_cards)


# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

game_end = False

while not game_end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(user_score)
    print(computer_score)

    if user_score == 0:
        print("You won the game")
        if computer_score == 0:
            print("Computer wins")
        if user_score > 21 or computer_score > 21:
            print("")

    # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    if user_score != 0 and computer_score != 0:
        choice_to_add_a_card = input("Do you want another card? Type 'yes' or 'no'").lower()
        
        if choice_to_add_a_card == 'yes':
            user_cards.append(deal_card())
            print(user_cards)
        else:
            game_end = True
            print("END")


# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.


# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
