# variables
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]

# Nested list
map = [row1, row2, row3]

# Print nested lists as a 3 * 3 matrix
print(f"{row1}\n{row2}\n{row3}")

# Holds the input
position = input("Where do you want to put the treasure? ")

# Get the two numbers for the input(position variable) by sub-scripting
# Ex: string[index] -- will hold the index of the string
input_1 = int(position[0]) # Will hold the first digit of input
input_2 = int(position[1]) # Will hold the second digit of input

# After separating the input into 2 different numbers input_1 and input_2
# Using the numbers to place the string 'X', as indexing of lists start from 0
# We subtracted 1 from both input_1 and input_2 
# Ex: input = 23
# input_1 = 2, input_2 = 3
# map[3 - 1, 2 - 1]
# map[2, 1] => 3rd list and 2nd item in that list (Indexing starts from 0)
map[input_2 - 1][input_1 - 1] = "X"

# ANOTHER WAY OF NAMING THE VARIABLES: (Same logic as above)
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizontal - 1] = "X"

# Print modified nested lists as a 3 * 3 matrix
print(f"{row1}\n{row2}\n{row3}")
