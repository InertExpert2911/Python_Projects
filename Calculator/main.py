# Importing replit to use clear() function.
from replit import clear

# Importing logo from art.
from art import logo

# Addition Function.
def add(n1, n2):
  return n1 + n2

# Subtraction Function.
def subtract(n1, n2):
  return n1 - n2

# Multiplication Function.
def multiply(n1, n2):
  return n1 * n2

# Division Function.
def divide(n1, n2):
  return n1 / n2

# Exponentiation Function.
def exponent(n1, n2):
  return n1 ** n2

# Dictionary to store all operators.
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": exponent,
}

# Function to calculate.
def calculator():
  # Printing the ASCII art from art.py
  print(logo)

  # Taking input from the user.
  num1 = float(input("What's the first number?: "))

  # For loop to print all Keys inside the dictionary.
  for symbol in operations:
    print(symbol)

  # Flag that controls the while loop.
  should_continue = True
 
  # While loop for calculator.
  while should_continue:

    # Getting input.
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    # Extracting the value from the dictionary with the help of its key.
    calculation_function = operations[operation_symbol]

    # Calling the functions of add, subtract, multiply, divide, exponent based on user input.
    answer = calculation_function(num1, num2)

    # Printing things.
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # This conditional is to check if the user wants to continue or start a fresh calculation.
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':

      # Sets the value of num1 to answer, so that we can continue the calucation with the previous result.
      num1 = answer

    # If the user inputs any other input.  
    else:
      # Modifying the flag to end while loop.
      should_continue = False

      # Clearing the screen, so that the user can start a new calculation
      clear()

      # Calling calculator() inside calculator() -- RECURSION 
      # RECURSION(A function that calls itself).
      # Helps us to start the function from the top again without us running the code again.
      calculator()


# Calling calculator fucntion to run all code inside the function.
calculator()


# https://replit.com/@TharunReddy5/Calculator