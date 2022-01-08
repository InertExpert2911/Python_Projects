# Importing random module
import random

print("Welcome to the game of Rock, Paper & Scissors!!")

# ASCII Art XD
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

# List of all game images
game_images = [rock, paper, scissors]

# Getting input from the user
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Printing user's choice and catching invalid input
if user_choice >= 3 or user_choice < 0:
  print("Invalid input")
else:
  print(game_images[user_choice])

  # Generating a number number for computer
  computer_choice = random.randint(0, 2)
  print("Computer chose:")

  # Printing computer's choice
  print(game_images[computer_choice])

  # WIN, LOSE & DRAW LOGIC
  if user_choice == computer_choice:
    print("It's a draw")
  elif user_choice == 0 and computer_choice == 2:
    print("You Win !!")
  elif user_choice == 1 and computer_choice == 0:
    print("You Win!!") 
  elif user_choice == 2 and computer_choice == 1:
    print("You Win !!")
  else:
    print("You Lose, Try again?")

# https://replit.com/@TharunReddy5/RockPaperScissors#main.py