# CHALLENGE - 2: REPLACE BLANKS WITH GUESSES

# Import random module
import random

# List that holds all words
word_list = ["aardvark", "baboon", "camel"]

# Choice function helps us to choose a random word from the above list
chosen_word = random.choice(word_list)
# print(type(chosen_word))

# Testing code
print(f'Psst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display

# Empty list
display = []

# Store the length of the chosen word
word_length = len(chosen_word)

# For each letter in the chosen_word, add a "_" to 'display'
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess

# Use _ (underscore), if you don't need to store the values from the loop
for _ in range(0, word_length):
    display += "_"

# -----------------------------------------------------------------------------------------------------------

# This will work just the same as above code

# for _ in range(word_length):
#     display += "_"

# -----------------------------------------------------------------------------------------------------------

guess = input("Guess a letter: ").lower()

# TODO-2: - Loop through each position in the chosen_word;

# If the letter at that position matches 'guess' then reveal that letter in the display at that position
# Eg: If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]

# Looping through the range of 0 to len(chosen_word) - 1
for position in range(0, word_length):
    # Use Subscripting to find if the letter at the index is same as user's guess
    if chosen_word[position] == guess:
        # If yes we are overwriting the index number with user's guess
        display[position] = guess
        
# -----------------------------------------------------------------------------------------------------------

# This will work just the same as above code
        
# for position in range(word_length):
#     letter = chosen_word[position]
#     # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter

# -----------------------------------------------------------------------------------------------------------

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"

print(display)

# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in challenge 3
