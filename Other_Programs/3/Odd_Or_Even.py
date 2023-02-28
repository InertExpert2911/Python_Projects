# Getting user input and converting the data type to an int
number = int(input("Which number do you want to check? "))

# % -- Modulo Operator, this returns the remainder after dividing two numbers
# Even numbers when divided by 2, gives remainder as 0
if number % 2 == 0:
    print("This is an even number.")
# Odd numbers return 1 as remainder after dividing by 2
else: 
    print("This is an odd number.")