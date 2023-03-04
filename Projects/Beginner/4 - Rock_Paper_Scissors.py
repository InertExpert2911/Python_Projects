# Import random module
import random

# Variables with ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List to store all ASCII variables defined above
ascii_art_list = [rock, paper, scissors]

# Get users choice and convert it into a int data type
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# Generate a random integer between 0 and 2 as indexing starts from 0
computer_choice = random.randint(0, 2)

# Catch when user typed a number higher than 3 or less than 0, as we don't have either at the start of the program
if user_choice >= 3 or user_choice < 0:
    print("You gave an invalid input, you lost.")

# Else to catch all other cases, where the input meets the conditions we set i.e (0, 1 and 2 only)
else:
    # Use the index from the input, and print that index from the list
    print(ascii_art_list[user_choice])

    print("Computer chose: \n")

    # Print the index value of the list
    print(ascii_art_list[computer_choice])

    # The outcome of the game is determined by 3 simple rules:
    # 1. Rock wins against scissors
    # 2. Scissors win against paper
    # 3. Paper wins against rock

    # Catch cases you win.
    if user_choice == 0 and computer_choice == 2:
        print("You won!")
    elif (user_choice == 1 and computer_choice == 0):
        print("You won!")
    elif user_choice == 2 and computer_choice == 1:
        print("You won!")
    # Catch cases when you and the computer chose same number
    elif user_choice == computer_choice:
        print("Draw, try again.")
    # Catch all lost cases
    else:
        print("You lost.")