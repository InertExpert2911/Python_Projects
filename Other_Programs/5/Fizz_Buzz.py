# Loops through numbers in range 1 to 100 (101 not included)
for number in range(1, 101):
    # Check conditions if the number is divisible by 3 and 5
    # number % 3 -- Returns the remainder after division, 0 means cleanly divisible, else it is not cleanly divisible
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Check condition if the number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    # Check condition if the number is divisible by 5
    elif number % 3 == 0:
        print("Fizz")
    # If none of the above cases satisfy, print just the number
    else:
        print(number)