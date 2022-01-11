# Importing random module
import random

# Variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")

# Taking input from the user
nr_letters = int(input("How many letters would you like in your password?\n")) 

nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_symbols = int(input(f"How many symbols would you like?\n"))

""" Eazy Level - Order not randomised:
e.g. 4 letter, 2 symbol, 2 number = JduE&!91 """

# List and an empty string
letters_list = []
letters_string = ''

# For loop to loop from 0 till the range of nr_letters
for letter in range(0, nr_letters):
  # random_letter is used to store the random number generated
  random_letter = random.randint(0, len(letters)-1)
  # Appending the random element to the list
  letters_list.append(letters[random_letter])

# Using letters_string using .join() on letters_list
# To store the string
letters_string = letters_string.join(letters_list)

numbers_list = []
numbers_string = ''

for number in range(0, nr_numbers):
  random_number =  random.randint(0, len(numbers)-1)
  numbers_list.append(numbers[random_number])

numbers_string = numbers_string.join(numbers_list)

symbols_list = []
symbols_string = ''

for symbol in range(0, nr_symbols):
  random_symbol = random.randint(0, len(symbols)-1)
  symbols_list.append(symbols[random_symbol])

symbols_string = symbols_string.join(symbols_list)
  
# Printing the entire password as a single string 
print((f"{letters_string}{numbers_string}{symbols_string}"))