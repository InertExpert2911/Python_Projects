# Importing modules.
from random import randint
from art import logo

# GLOBAL VARIABLES.
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# To check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """Checks the answer against guessed number and returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


# To set the game difficulty.
def set_difficulty():

  game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if game_difficulty == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

# The Number Guessing Game.
def number_guessing_game():

  # Printing ASCII Art.
  print(logo)

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  # Choosing a random integer from 1 to 100 (100 inclusive).
  answer = randint(1, 100)

  # **********FOR TESTING PURPOSES ONLY**********
  # print(f"Pssst, the correct answer is {answer}") 
  # **********FOR TESTING PURPOSES ONLY**********

  # This variable will hold the number of turns based on the difficulty.
  turns = set_difficulty()

  guess = 0

  # Repeating the loop till the user guesses the answer. 
  while guess != answer:

    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    # check_answer() will check the user's guess and prints 'too low' or 'too high' and also returns the turns subtracted by 1. We are updating the turns value by storing it back in turns again.
    turns = check_answer(guess, answer, turns)

    # Checking if the user has no turns left.
    if turns == 0:
      print("You've run out of guesses, you lose.")
      # To exit out of the loop.
      return
    # OPTIONAL.
    elif guess != answer:
      print("Guess again.")

# Calling the function.
number_guessing_game()

# https://replit.com/@TharunReddy5/GuessTheNumber#main.py