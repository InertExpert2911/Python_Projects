# Guess a randomly generated number between 1 and 100.

# Import random module
from random import randint
import random

# Import logo
from number_guessing_game_logo import logo

# FUnction to generate and return a random number


def random_number_generator():
    """Returns a random integer number between 1 and 100, inclusive of both numbers."""

    # Get a random integer between 1 and 100 (both inclusive)
    return random.randint(1, 100)

# Function to compare user guess and randomly generated number from above function


def compare_guess(generated_number):
    """Handles user guess and returns "Too High" or "Too Low" or if the user found the number based on users guess. 
    Takes an integer as an input. Here we are working with randomly generated number"""

    # Get input
    user_guess = int(input("Make a guess: "))

    # Allow the player to submit a guess for a number between 1 and 100
    if user_guess >= 1 and user_guess <= 100:

        # Check user's guess against actual answer, depending on the user's guess
        if user_guess == generated_number:
            # 0 represents that the user guessed the correct number
            return 0
        elif user_guess > generated_number:
            return "Too High."
        elif user_guess < generated_number:
            return "Too Low."
    else:

        # If user doesn't enter a number in the range, return below string
        return "Your guess is out of the range, guess a number between 1 and 100."

# Function to hold the logic of the guessing game


def number_guessing_game():
    """Holds number guessing game logic."""

    # Track the number of turns remaining
    user_lives = 0

    # ASCII ART
    print(logo)

    print("Welcome to the number guessing game!")
    print("I'm thinking a number between 1 and 100.")

    # Store the randomly generated number
    random_number = random_number_generator()

    # Result
    # print(f"Psst, the number I guessed is {random_number}")

    # Two different difficulty levels (10 guesses in easy mode, only 5 guesses in hard mode)
    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # Update user_lives based on input
    if game_difficulty == 'easy':
        user_lives += 10
    elif game_difficulty == 'hard':
        user_lives += 5
    else:
        print("Invalid input")

    # Loops based on user_lives value
    while user_lives >= 1:

        # Provide feedback of number of lives left to the player
        print(f"You have {user_lives} attempts remaining to guess the number.")

        # Store the returned values for compare_guess function
        compare_user_guess = compare_guess(random_number)

        # Check the returned values from compare_guess() function
        if compare_user_guess == 0:

            # Update user_lives to 0 to stop the loop and end the game
            user_lives = 0

            # If the user got the answer correct, show the guessed number
            print(f"You got the number! The number was {random_number}")
        else:
            # Deduct user_lives by 1 for every iteration
            user_lives -= 1

            # Print whatever is returned
            print(compare_user_guess)
            
            # Catch when user_lives turns to 0 and print the below line to let the user know
            if user_lives == 0:
                print(f"You ran out of lives. The number is {random_number}.")
                
                # Return can end/exit the function (Redundant code), just wanted to learn that we can use just return to exit out of function
                return
            else:
                print("Guess again.")


# Call the function to start the game
number_guessing_game()


# --------------------------------------------------- ANOTHER WAY ------------------------------------------------

# GLOBAL VARIABLES
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# # Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")


# # Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS


# def game():
#   print(logo)
#   # Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Psst, the correct answer is {answer}")

#   turns = set_difficulty()
#   # Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     # Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     # Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()

# --------------------------------------------------- ANOTHER WAY ------------------------------------------------
