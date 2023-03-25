# A simple calculator program capable of doing simple calculations with basic operators

import os
from calculator_logo import logo

# Function to add two numbers and returns the result
def add (num_1, num_2):
    return num_1 + num_2

# Subtract two numbers and returns the result
def subtract (num_1, num_2):
    return num_1 - num_2

# Divide two numbers and returns the result
def divide (num_1, num_2):
    return num_1 / num_2

# Multiply two numbers and returns the result
def multiply (num_1, num_2):
    return num_1 * num_2

def exponential (num_1, num_2):
    return num_1 ** num_2

# A dictionary that holds symbols as keys and names of the above functions as values
operations = {
                '+' : add,
                '-' : subtract,
                '/' : divide,
                '*' : multiply,
                '**' : exponential
            }

# Function that performs the calculation of two numbers
def calculator():

    # Print logo
    print(logo)

    # Inputs
    number_1 =  float(input("What's the first number?: "))

    # Loop through the dictionary and print all the keys
    for _ in operations:
        # Use an "_", when you don't have to store the values, we are just printing keys of the dictionary here
        print(_)

    # ---------------------------------- Above for loop works just the same as this on ---------------------------------
    # for symbol in operations:
    #     print(symbol)
    # ---------------------------------- Above for loop works just the same as this on ---------------------------------

    # Variable to control the while loop
    program_end = False

    # Loops till the user type 'n' or anything as input for wants_to_continue variable 
    while not program_end:
        
        # Get the operation the user want to perform
        operation_symbol = input("Pick an operation from the above line: ")

        # Inputs
        number_2 = float(input("What's the next number?: "))

        # Eg:
        # function = operations["+"]
        # print(function(2, 3))

        # Get hold of the name of function based on the key from the dictionary
        calculation_function = operations[operation_symbol]

        # Answer stores the value returned from the function
        result = calculation_function(number_1, number_2)

        # Print result
        print(f"{number_1} {operation_symbol} {number_2} = {result}")
        
        # Check if the user want to perform more operations on the result after first calculation
        wants_to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.: ")
        
        # Check condition
        if wants_to_continue == 'y':
            # This line will help us to update the first_answer for every iteration where user gives input as 'y'
            number_1 = result
            
        else:
            # To clear the screen
            os.system('cls')
            
            # End the loop if the user typ[e anything other than 'y'
            program_end = True
            
            # RECURSION: A function calling itself, Also make sure you have some conditions to stop a function calling itself endlessly
            calculator()

# Call the function
calculator()