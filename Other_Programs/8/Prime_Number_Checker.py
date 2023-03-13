# Prime numbers are numbers that can be cleanly divisible only by 1 and itself

# Create a function that checks if a number is prime or not by taking a number as a parameter
def prime_number_checker(number):
    
    # A  variable that hold a boolean
    is_prime = True
    
    # Loops through range 2 to number -1
    for i in range(2, number):
        
        # Check if any of the number is divisible completely giving no remainder
        if number % i == 0:
            # Update the boolean if the number is divisible
            is_prime = False
    
    # Based on the Boolean we print if it s prime or not        
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Get the inputs from the user
n = int(input("Check this number: "))

# Call the function that checks if the given number is prime or not
prime_number_checker(number=n)
