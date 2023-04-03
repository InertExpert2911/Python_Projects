
import random
from number_guessing_game_logo import logo


def random_number_generator():
    """Returns a random integer number between 1 and 100, inclusive of both numbers."""
    
    return random.randint(1, 100)


def compare_guess():
    """Handles user guess and returns "Too High" or "Too Low" or if the user found the number based on users guess"""
    
    user_guess = int(input("Make a guess: "))
    
    if user_guess == random_number:
        return f"You got the number! The number was {random_number}"
    elif user_guess > random_number:
        return "Too High."
    elif user_guess < random_number:
        return "Too Low."





user_lives = 0

# print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking a number between 1 and 100.")

random_number = random_number_generator()

print(f"Psst, the number I guessed is {random_number}")

game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if game_difficulty == 'easy':
    user_lives = 10
elif game_difficulty == 'hard':
    user_lives = 5
else:
    print("Invalid input")
    \

while user_lives != 0:
    
    print(f"You have {user_lives} attempts remaining to guess the number.")
    
    print(compare_guess())
    
    user_lives -= 1



