# The Cipher Encrypts and Decrypts the user input by the shift amount.
# ------------------------------------------ EXAMPLE --------------------------------------------
# Example: If your input for encode function is 'apple', shift_amount = 2
# ENCODE: 'crrng'
# If your input for decode function is 'crrng', shift_amount = 2
# DECODE: 'apple'
# ------------------------------------------ ANOTHER METHOD --------------------------------------------

# Function to encrypt and decrypt. with parameters
def caesar(input_text, shift_amount, input_direction):

    # Empty string
    output_text = ""

    # Loops through every letter of the input_text
    for char in input_text:
        
        # If we find a character in input_text that is present in alphabet lis
        if char in alphabet:
            
            # Get the index position of the letter form the list
            index_position = alphabet.index(char)

            # Check if the user is asking to encode or decode
            if input_direction == "encode":
                # Increase the shift amount based on user input
                index_position += shift_amount
            elif input_direction == "decode":
                # Decrease the shift amount based on user input
                index_position -= shift_amount

            # Add each letter based on the index position to the empty string variable
            output_text += alphabet[index_position]
            
        # For all other characters in the input_text (symbols, spaces and numbers)
        else:
            
            # Add char to the output_text
            output_text += char
            
    # Print output
    print(f"The {input_direction}d text is {output_text}")

# Import and print the logo, when the program starts
from caesar_logo import logo
print(logo)

# list that holds all alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# A variable to control while loop
program_control = False

# While loop that continues to execute the program if the user types 'yes'
# Loops till program_control is False, stops only when it is changed to True
while not program_control:
    
    # Variables to hold inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # If the user enters a shift that is greater than the number of letters in the alphabet list
    if shift >= 26:
        # Get the remainder of (shift / 26), so that shift always stays within the bounds no matter the shift
        shift %= 26
        # print(shift)
    
    # Call the function and pass arguments
    caesar(input_text = text, shift_amount = shift, input_direction = direction)
    
    # Store user input if they want to restart or not
    program_restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    # Type 'yes' if you want to go again. Otherwise type 'no'
    # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again
    if program_restart == 'yes':
        # Keep the same value as we need the loop to run
        program_control = False
    else:
        # If user types any other input other than 'yes'. example 'no'
        print("Goodbye")
        # Change the while loop control variable to stop the loop
        program_control = True
        
    # ------------------------------------------ ANOTHER METHOD --------------------------------------------
    
    # program_restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    # if program_restart == "no":
    #     program_control = True
    #     print("Goodbye")
    
    # ------------------------------------------ ANOTHER METHOD --------------------------------------------
