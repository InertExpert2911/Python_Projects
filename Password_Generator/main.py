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

""" Easy Level - Order not randomised:
e.g. 4 letter, 2 symbol, 2 number = JduE&!91 """


'''

# A password string
password = ''

# For loop to loop from 0 till the range of nr_letters
for letter in range(0, nr_letters):
  # Concatenating the random letter to password
  password += random.choice(letters)
  
  # THIS WORKS TOO
  # random_letter is used to store the random letter generated
  # random_letter = random.choice(letters)
  # password += random_letter

for number in range(0, nr_numbers):
  password += random.choice(numbers)
  # THIS WORKS TOO
  # random_number =  random.choice(numbers)
  # password += random_number

for symbol in range(0, nr_symbols):
  password += random.choice(symbols)
  
# Printing the password
print(password)

'''

""" Hard Level - Order of characters randomised:
e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P """

password_list = []

for letter in range(0, nr_letters):
  password_list.append(random.choice(letters))

for number in range(0, nr_numbers):
  password_list.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
  password_list.append(random.choice(symbols))

# Suffleing the items in the list
random.shuffle(password_list)

# A for loop to concatenate all the charcters into password variable 
password = ""
for char in password_list:
  password += char

print(f"Your strong password is {password}")

# https://replit.com/@TharunReddy5/PasswordGenerator#main.py
