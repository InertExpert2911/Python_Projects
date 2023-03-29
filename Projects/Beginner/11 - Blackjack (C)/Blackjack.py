# A game of Blackjack

# Read this breakdown of program requirements or the flowchart, if needed:
# http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF


# Import random module
import random

import os

# Import logo
from blackjack_logo import logo

# Function that uses the List below to return a random card, 11 is the Ace
def deal_card():
    """Returns a random card from the deck."""
    
    # Cards list
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    # Choice() helps us to get a random item from a list
    return random.choice(cards)


# Function returns the score after calculation
def calculate_score(list_of_cards):
    """Calculates the sum of all the cards in the inputted list and returns the score."""
    
    # sum() returns the sum of all the items from the list
    score = sum(list_of_cards)
    
    # Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score
    if score == 21 and len(list_of_cards) == 2:
        # 0 will represent a blackjack in our game
        return 0
    
    # Check for an 11 (ace)
    # If the score is already over 21, remove the 11 and replace it with a 1
    if 11 in list_of_cards and score > 21:
        
        list_of_cards.remove(11)
        list_of_cards.append(1)
        
        # Another way can be to get the index and replace the item at that specific index
        # index_of_ace = list_of_cards.index(11)
        # list_of_cards[index_of_ace] = 1
    
    return score

# Function checks user's and computer's score and returns a string based on the condition
def compare(user_cards_score, computer_cards_score):
    
    """Checks all the below conditions and returns a string:
    1. If the computer and user both have the same score, then it's a draw. 
    2. If the computer has a blackjack (0), then the user loses. 
    3. If the user has a blackjack (0), then the user wins. 
    4. If the user_score is over 21, then the user loses. 
    5. If the computer_score is over 21, then the computer loses, you win.
    6. If none of the above, then the player with the highest score wins.
    """
    # Check the conditions and returns a string with output
    if user_cards_score == computer_cards_score:
        return "Draw 🙄"
    
    elif computer_cards_score == 0:
        return "You lost, Computer has Blackjack 😅 "
    
    elif user_cards_score == 0:
        return "You won with a Blackjack 👌"
        
    elif user_cards_score > 21:
        return "Your score went over 21, you lost the round 🤦‍♂️"
    
    elif computer_cards_score > 21:
        return "Computer score went over 21, you won the round 😁"
    
    elif user_cards_score > computer_cards_score:
        return "You won 👍"
    
    else:
        return "You lost 😐"

# Function to play the game of blackjack
def play_game_of_blackjack():
    
    """
    ############### Our Blackjack House Rules #####################
    
    1. The deck is unlimited in size.
    2. There are no jokers.
    3. The Jack/Queen/King all count as 10.
    4. The the Ace can count as 11 or 1.
    5. Use the following list as the deck of cards:
    6. cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    7. The cards in the list have equal probability of being drawn.
    8. Cards are not removed from the deck as they are drawn.
    9. The computer is the dealer.
    
    ############### Our Blackjack House Rules #####################
    """
    
    # Print logo
    print(logo)
    
    # Empty lists to store randomly generated cards
    user_cards = []
    computer_cards = []
    
    # Deal the user and computer 2 cards each using deal_card() and append()
    for _ in range (0, 2):
        # Append the randomly chosen cards to the empty list
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    # Variable to control the while loop
    game_over = False
    
    # Loops till game_over is True
    while not game_over:
        
        # Score will need to be rechecked with every new card drawn and need to be repeated until the end.
        
        # Calculate the score of user and computer cards
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
        
        # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends
        if user_score == 0 or computer_score == 0 or user_score > 21:
            # End the loop and the game
            game_over = True
        else:
            # If the game has not ended, ask the user if they want to draw another card
            # If yes, then use the deal_card() function to add another card to the user_cards List
            # If no, then the game has ended
            
            # Get input
            choice_to_add_a_card = input("  Do you want another card? Type 'y' or 'n': ").lower()
            
            if choice_to_add_a_card == 'y':
                # Add the new card to the user_cards list
                user_cards.append(deal_card())
                # print(user_cards)
            else:
                # End the game  if user gives any input other than 'y'
                game_over = True
    
    # Computer should keep drawing cards as long as it has a score less than 17
    while computer_score != 0 and computer_score < 17:
        # Add the cards to the computer_cards list
        computer_cards.append(deal_card())
        # Re-calculate computer score to update
        computer_score = calculate_score(computer_cards)
    
    # Call the compare function to get a result of who won the round
    game_result = compare(user_score, computer_score)
    
    # Print results
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final_score: {computer_score}")
    print(game_result)

# Ask the user if they want to start the game
# If they answer yes, clear the console and start a new game of blackjack
while input("  Do you want to play a round of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    
    # Clear screen
    os.system('cls')
    
    # Call the function to play another round
    play_game_of_blackjack()