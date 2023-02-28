# Importing random module
import random

names_string = input("Give me everybody's names, separated by a comma. ")

# str.split("symbols or parameters you want to split by") method converts a string into a list, based on the parameters you define
# In the below case, it uses (", ") comma followed by a space to divide the string and make it into a list
names = names_string.split(", ")

# Ex: INPUT: Tharun, Giri, Moni >>> OUTPUT: ['Tharun','Giri','Moni']
# print(names)

# Get the length of the list
total_number_of_persons = len(names)

# Using randint() function to generate a number from 0, which is the start of the index to length of index - 1 (As indexing starts from 0)
random_choice = random.randint(0, (total_number_of_persons - 1))

# Get the name from the list and print it with f-strings
print(f"{names[random_choice]} is going to buy the meal today!")

# Another method to solve this is by using below lines opf code
# You can use these 2 lines instead of line 14, 17 and 20

# random.choice(seq) is a function, wherein you would want to randomly pick up an item from a List/sequence.
# random_choice = random.choice(names)
# print(f"{random_choice} is going to pay the meal today!")
