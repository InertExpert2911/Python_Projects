# List that holds all alphabets
# Alphabets are repeated twice to handle index out of bounds errors
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# We are not using this in this file
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Get the input and convert it to lowercase as we have letters in the list are lowercase
text = input("Type your message:\n").lower()

# Get the shift and convert to int
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs

# A function to encrypt(move) the text by a given shift
def encrypt (plain_text, shift_amount):
    
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text
    
    # ------------------------------------------ Example ----------------------------------------------------------
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"
    # ------------------------------------------ Example ----------------------------------------------------------
    
    # An empty string to hold output
    cipher_text = ""
    
    # Loops through every letter in the inputted text
    for letter in plain_text:
        
        # Get the index of the letter using .index() function which gets the first occurrence in a list and store that data in text_index variable
        text_index = alphabet.index(letter)
        
        # Increase the index by shift given the user
        text_index += shift_amount
        
        # Condition to handle index is out of bounds error
        # Another easy method to handle this is by adding another set of items from 'a' to 'z' in alphabets list
        # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛 -- FIXED (Kinda)
        # if text_index >= len(alphabet):
        #     # Goes to the start of the list if the text_index is > 25
        #     text_index = 0
        #     text_index += shift_amount
        
        
        
        
        # Add each letter looped to the variable cipher_text
        cipher_text += alphabet[text_index]  
        
    # Print result
    print(f"The encoded text is {cipher_text}")

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message

# Using keyword arguments as input when calling the function
encrypt(plain_text = text, shift_amount = shift)
