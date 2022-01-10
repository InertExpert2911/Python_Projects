# Using range(start, end (not included))
for number in range(1, 101):
    
    # Checking if a number is divisible by 3 & 5
    # We want this condition to be front because if,elif will stop once a condition is true
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Checking if a number is divisible by 3
    elif number % 3 == 0:
        print("Fizz")
    # Checking if a number is divisible by 3
    elif number % 5 == 0:
        print("Buzz")
    # Printing the number if the above cases fail
    else:
        print(number)