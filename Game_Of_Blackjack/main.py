# Importing random module.
import random

# Importing clear() from replit module.
from replit import clear

# Importing logo from art.py
from art import logo


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  # Using choice() to pick a random card from the list.
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Takes a list of cards as input and returns the score calculated from the sum of the cards"""

  # Sum of all cards in the list inputted to calculate_score(list_of_cards)
  score = sum(cards)

  # Checking for Blackjack(sum = 21) with only 2 cards
  if score == 21 and len(cards) == 2:
    return 0 #(0 means BLackjack)

  # Checking from an Ace(11) and if the sum is over 21. We will remove Ace(11) from the cards list and append 1 as the value of Ace.
  if 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
  return score


def compare(user_score, computer_score):
  """Compares user score and computer score and check who won the Blackjack"""

  # If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  # If the computer has a blackjack (0), then the user loses.
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  # If the user has a blackjack (0), then the user wins.
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  # If the user_score is over 21, then the user loses.
  elif user_score > 21:
    return "You went over. You lose 😭"
  # If the computer_score is over 21, then the computer loses.
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  # If user score is greater than computer score, then the users wins.
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
  """Plays the game of Blackjack"""

  # logo from art.py
  print(logo)

  # Empty lists to hold the randomly drawn cards.
  user_cards = []
  computer_cards = []

  # Flag to check if the game is over or not.
  is_game_over = False

  # To append 2 randomly drawn cards into the empty list created above.
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  # Checking the score everytime a card is drawn until game is over.
  while not is_game_over:

    # Calling calculate_score function to find out the sum of the cards.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Printing
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    if user_score == 0 or computer_score == 0 or user_score > 21:
      # Ending the game.
      is_game_over = True
    else:
      # Drawing a new card for the user.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        # Ending the game.
        is_game_over = True

  # The computer should keep drawing cards as long as it has a score less than 17 and not equal to 0 (Blackjack).
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    # Updating the computer score for every card drawn.
    computer_score = calculate_score(computer_cards)

  # Printing
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


# To make the user play the game repeatedly.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

# https://replit.com/@TharunReddy5/Blackjack#main.py