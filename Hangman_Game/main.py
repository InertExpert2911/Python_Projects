import random
from hangman_art import stages, logo
from hangman_words import word_list

# To clear the screen after each guess.
from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code.
# print(f'Pssst, the solution is {chosen_word}.')

# Creating blanks.
display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    # Making use of the clear() to clear screen after each guess.
    clear()

    # If the user has entered a letter they've already guessed, printing the letter.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    # Checking if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, printing the letter and letting the user know.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    # Checking if the user has got all letters in chosen_word.
    if not "_" in display:
        game_is_finished = True
        print("You win.")
    
    # Printing the ASCII Art.
    print(stages[lives])
