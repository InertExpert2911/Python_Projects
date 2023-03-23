
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

# A dictionary that holds symbols as keys and names of the above functions as values
operations = {
                '+' : add,
                '-' : subtract,
                '/' : divide,
                '*' : multiply,
            }



# TODO-1: Print logo


# Inputs
number_1 = int(input("What's the first number?: "))

# Loop through the dictionary and print all the keys
for _ in operations:
    # Use an "_", when you don't have to store the values, we are just printing keys of the dictionary here
    print(_)

# ---------------------------------- Above for loop works just the same as this on ---------------------------------
# for symbol in operations:
#     print(symbol)
# ---------------------------------- Above for loop works just the same as this on ---------------------------------

# Get the operation the user want to perform
operation_symbol = input("Pick an operation from the above line: ")

# Inputs
number_2 = int(input("What's the second number?: "))

# Eg:
# function = operations["+"]
# print(function(2, 3))

# Get hold of the name of function based on the key from the dictionary
calculation_function = operations[operation_symbol]

# Answer stores the value returned from the function
first_answer = calculation_function(number_1, number_2)

# Print result
print(f"{number_1} {operation_symbol} {number_2} = {first_answer}")


# Variable to control the while loop
program_end = False

# Loops till the user type 'n' or anything as input for wants_to_continue variable 
while not program_end:
    
    # Check if the user want to perform more operations on the result after first calculation
    wants_to_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.: ")
    
    # Check if the input is 'y'
    if wants_to_continue == 'y':

        # Ask the user to pick an operation
        operation_symbol = input("Pick another operation: ")
        
        # Create a new variable to store another number
        number_3 = int(input("What's the number?: "))
        
        # Get the value from the key and call he function using that value
        calculation_function = operations[operation_symbol]
        
        second_answer = calculation_function(first_answer, number_3)
        
        
        print(f"{first_answer} {operation_symbol} {number_3} = {second_answer}")
        
    else:
        # End the loop if the user typ[e anything other than 'y'
        program_end = True
