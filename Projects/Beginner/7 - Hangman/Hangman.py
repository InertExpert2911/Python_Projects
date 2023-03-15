# Module to clear screen
import os

# Import random module
import random

# Delete this line: word_list = ["aardvark", "baboon", "camel"]

# Import words from hangman words file
import hangman_words

# Chose a random word from a huge list of words
chosen_word = random.choice(hangman_words.word_list)

# Get the length of randomly chosen word
word_length = len(chosen_word)

# Variable to control while loop
end_of_game = False

# Holds the number of guesses we want to give to the user
lives = 6

# Get logo and stages from the hangman art file
from hangman_art import logo, stages
print(logo)

# Testing code 
# print(f'Psst, the solution is {chosen_word}.')

# Empty list to hold blanks
display = []

# Fills the list with number of blanks based on the word length
for _ in range(word_length):
    display += "_"

# Loops till end_of_game is True
while not end_of_game:
    
    # Input from the user
    guess = input("Guess a letter: ").lower()
    
    # To clear the screen
    os.system('cls')

    # If the user has entered a letter they've already guessed, print the letter and let them know (the letter that the user got right)
    
    # Let the user know if they guessed a letter that is already guessed, which is present in display list
    if guess in display:
        print(f"You have already guessed letter '{guess}'")
    
    # Check guessed letter
    for position in range(word_length):
        # Letter gets the letters of the chosen word one by one as for loops starts to iterate based on the word length of the chosen word
        letter = chosen_word[position]
        
        # Test code
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        
        # Condition to check if letter and user guess is same, if yes then update display list
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        
        # Simple hint to the user
        print(f"You guessed letter '{guess}', that's not in the word. You lost a life.")
        
        # Decrease the lives by 1 as user guessed wrong letter
        lives -= 1
        
        # Condition to check if the lives hold 0, if yes then end game
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    # Printing the hangman art every iteration
    print(stages[lives])
