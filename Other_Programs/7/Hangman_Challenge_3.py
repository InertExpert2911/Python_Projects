# CHALLENGE - 3: CHECK IF THE PLAYER HAS WON THE GAME


import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Psst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# A variable to control the while loop
end_of_game = False

# Loops till end_of_game value is true
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # A simple print statement to print the position, guess and letter in the for loop (f-strings)
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
    
    # Modifying end_of_game variable to stop while loop when it achieves this condition 
    if  not '_' in display:
        # Change the value of the variable to True to stop while loop
        end_of_game = True
        print("You Won!!")

# -----------------------------------------------------------------------------------------------------------

# METHOD - 1: 

# Checks for every iteration if '_' is present is list display, runs till it finds no, in that case the loop is stopped
# while '_' in display:
#     guess = input("Guess a letter: ").lower()

#     # Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # A simple print statement to print the position, guess and letter in the for loop
#         #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     print(display)

# -----------------------------------------------------------------------------------------------------------
