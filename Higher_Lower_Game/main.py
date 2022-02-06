import random
from art import logo, vs, game_over
from game_data import data
from replit import clear


def get_random_account():
  """Gets a random account from data in game_data.py."""
  return random.choice(data)

def format_data(account):
  """Takes the account data and returns in a printable format."""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, followers_a, followers_b):
  """Takes the user's guess and follower count and returns if the user got it right (returns a Boolean)."""
  if followers_a > followers_b:
    return guess == "a"
  else:
    return guess == "b"



def higher_lower_game():
  """Play Higher Lower Game."""
  print(logo)

  # To track user's score.
  user_score = 0

  # Flag to handle while loop.
  is_game_over = False

  # Storing random accounts in a variable.
  account_a = get_random_account()
  account_b = get_random_account()

  # To run the game till the user's guess is wrong.
  while not is_game_over:
    # We are moving the account_b contents to account_a.
    account_a = account_b
    # We are Regenarating account_b everytime the loop runs, so we see different users each time.
    account_b = get_random_account()

    # Regenarate account_b till both accounts are no longer same.
    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Getting the input.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Getting the follower count from data.
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    # Storing the returned Boolean
    is_correct = check_answer(guess, follower_count_a, follower_count_b)

    # Clearing the screen
    clear()
    print(logo)

    # Checking if the user's input is correct.
    if is_correct:
      # Incrementing score.
      user_score += 1
      print(f"You're right! Current score: {user_score}.")
    else:
      clear()
      is_game_over = True
      print(game_over)
      print(f"Sorry, that's wrong. Final score: {user_score}.")


# Calling the function to run the game.
higher_lower_game()

# https://replit.com/@TharunReddy5/HigherLowerGame#main.py

'''
NOTE: We are making choice B always become choice A in every round,even when A had more followers 
EXAMPLE: Suppose you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. XD
'''