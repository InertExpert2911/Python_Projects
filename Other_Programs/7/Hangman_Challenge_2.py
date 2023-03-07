# CHALLENGE - 2: REPLACE BLANKS WITH GUESSES

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# print(type(chosen_word))

# Testing code
print(f'Psst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display

# Empty list
display = []

# For each letter in the chosen_word, add a "_" to 'display'
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess
for letter in range(0, len(chosen_word)):
    display += "_"

# print(display)

guess = input("Guess a letter: ").lower()

# # TODO-2: - Loop through each position in the chosen_word;

# # If the letter at that position matches 'guess' then reveal that letter in the display at that position
# # Eg: If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]
for num in range(0, len(chosen_word)):
    for char in chosen_word:  
        if char == guess:
            display[num] = char
        

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"

print(display)

# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3
