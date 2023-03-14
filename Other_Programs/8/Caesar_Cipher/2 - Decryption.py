# Alphabets are repeated twice to handle index out of bounds errors
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Variables to store inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encryption
def encrypt (plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# Decryption
def decrypt (cipher_text, shift_amount): 
    
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # ------------------------------------------ Example ----------------------------------------------------------
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"
    # ------------------------------------------ Example ----------------------------------------------------------

    # An empty string to hold output
    decrypt_text = ""
    
    # Loops through every letter in the inputted text
    for letter in cipher_text:
      
      # Get the index of the letter using .index() function which gets the first occurrence in a list and store that data in index variable
      text_index = alphabet.index(letter)
      
      # Decrease the index by shift provided the user
      text_index -= shift_amount
      
      # Add each letter looped to the variable decrypt_text
      decrypt_text += alphabet[text_index]
    
    # Print result
    print(f"The decoded text is {decrypt_text}")
    

# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# Call the functions based on the input user gives
if direction == "encode":
  # Encryption
  encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
  # Decryption
  decrypt(cipher_text = text, shift_amount = shift )
else:
  print("Wrong input")
