# List of all alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# variables to store inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# Function to encrypt and decrypt text
def caesar(input_text, shift_amount, input_direction):
    
    # Empty string
    output_text = ""

    # Loops through every letter of the input_text
    for letter in input_text:
        
        # Get the index position of the letter form the list
        index_position = alphabet.index(letter)
        
        # Check if the user is asking to encode or decode
        if input_direction == "encode":
            # Increase the shift amount based on user input
            index_position += shift_amount
        elif input_direction == "decode":
            # Decrease the shift amount based on user input
            index_position -= shift_amount
        
        # Add each letter based on the index position to the empty string variable 
        output_text += alphabet[index_position]
    
    # Print output
    print(f"The {input_direction}d text is {output_text}")
    

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# Call the function
caesar(input_text=text, shift_amount=shift, input_direction=direction)


# -------------------------------------------------- Another Method ---------------------------------------------------

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"Here's the {direction}d result: {end_text}")
    

# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# -------------------------------------------------- Another Method ---------------------------------------------------


# -------------------------------------------------- Long Method --------------------------------------------------- 

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")


# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

# -------------------------------------------------- Long Method ---------------------------------------------------

