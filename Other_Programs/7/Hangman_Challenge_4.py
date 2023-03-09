# CHALLENGE - 4: KEEP TRACK OF PLAYER'S LIVES IN THE GAME (FOR CHALLENGE - 5: IMPROVE UI (Refer: Python_Projects\Projects\Beginner\7 - Hangman\7 - Hangman.py)


import random

# List to hold ASCII art of the game
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Variable to control the loop
end_of_game = False

# Other useful variables
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left

# Set 'lives' to equal 6 (The total number of lives the user has)
lives = 6

# Testing code
print(f'Psst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Loop till end_of_game is True
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # TODO-2: - If guess is not a letter in the chosen_word,
    
    # Then reduce 'lives' by 1
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    # Another way for the below condition cloud be: (if guess not in chosen_word:)
    if letter != guess:  
        # Decrease the value of lives by 1
        lives -= 1 
        # Checks if lives is 0, if yes then stop the while loop as we change the end_of_game to True
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list display and turn it into a String
    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining
    
    # Print the art from the list stages based on the value of lives variables
    print(stages[lives])
    
    

