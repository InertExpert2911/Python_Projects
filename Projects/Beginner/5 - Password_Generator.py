# Import Random module
import random

# Variables to hold all letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome print statement
print("Welcome to the PyPassword Generator!")

# Get inputs from the user (how many numbers or letters or symbols they want in their password) and convert it into int data type
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# ----------------------------------------------------------------------------------------------------------

# METHOD - 1: Easy - Order of characters in the password is not randomized:
# Eg: 4 letter, 2 symbol, 2 number = JduE&!91

# Empty string to hold all the values generated
password_generated = ""

# Loops through the range from 0 to the number inputted by the user - 1, as in range() function end is not inclusive in the range
for letter in range(0, nr_letters):
    # random.choice(sequence) --- Chooses a random item from the sequence
    # Concatenate that choice returned above to the password_generated variable
    password_generated += random.choice(letters)
    # print(password_generated)

for symbol in range(0, nr_symbols):
    password_generated += random.choice(symbols)
    # print(password_generated)

for number in range(0, nr_numbers):
    password_generated += random.choice(numbers)
    # print(password_generated)

# Print password
print(f"Your password can be: {password_generated}")

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------

# METHOD - 2: Hard - Order of characters in the password is randomized:
# Eg: 4 letter, 2 symbol, 2 number = g^2jk8&P

# random.sample(string, len(string)) returns a list even when a string or tuple is specified to the first argument, so it is necessary to convert it to a string or tuple.
# For strings, a list of characters is returned. Use the join() method to concatenate to a single string again.
shuffled_password = ''.join(random.sample(
    password_generated, len(password_generated)))

# Print shuffled password
print(f"Your shuffled password is: {shuffled_password}")

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------
# METHOD - 2.1:

# password_generated_list = [] -- Variable to store items in a list

# Same logic of for loops as above
# for number in range(0, nr_numbers):
#     password_generated_list += random.choice(numbers)

# OR different for-loop logic with list can be by using .append()
# for number in range(0, nr_numbers):
#     password_generated_list.append(random.choice(numbers))

# random.shuffle(password_generated_list) -- Shuffles the items in a list and updates the list

# password = ""
# Loops through each item in a list and concatenated to the string defined above
# for char in password_generated_list:
#   password += char

# print(password) -- Prints the shuffled password

# ----------------------------------------------------------------------------------------------------------
