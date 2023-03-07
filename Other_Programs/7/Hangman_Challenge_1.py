# CHALLENGE - 1: PICK RANDOM WORD AND CHECK

# Importing random module
import random

# List of words
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word

# Use choice() function to choose a random word from the list
chosen_word = random.choice(word_list)

# Print randomly chosen word, just so that we know which word was chosen
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

# Store user's input and convert it to lowercase
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word

# Loops through each letter in the randomly chosen word
for letter in chosen_word:
    # Compares if the letter and user's guess is same
    if letter == guess:
        # If TRUE print this
        print("Right")
    else:
        # If FALSE print this
        print("Wrong")
