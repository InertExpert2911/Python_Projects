# Has two sets of alphabets because of the shift_amount.
# Ex: zulu --> Out Of Bounds Error if you have one set. So 2 sets to overcome it.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encode and decode the input.
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""

  # If stmt to check and multiply the amount with -1 as we have to do the below operation to decode.
  # new_position = position - shift_amount
  if cipher_direction == "decode":
    shift_amount *= -1
    
  for char in start_text:
    # Finding the index of the char in alphabet then modifying it to a new alphabet.
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    # To preserve any other character that is not present in alphabet.
    else:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")

# Importing the logo from art
from art import logo
print(logo)

# Flag to control the while loop.
should_end = False

# To run the loop till user says to stop.
while not should_end:

  # Taking input from the user.
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # If user enters a shift > 26, We divide it by 26 and use the remainder as shift.
  shift = shift % 26

  # Calling the function with arguments.
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  # To restart the program if the user wants to.
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    
# https://replit.com/@TharunReddy5/CaesarCipher#main.py

