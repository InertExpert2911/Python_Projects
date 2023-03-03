# Modules - Holds pieces of code that can perform various functions
# random module can help us generate pseudo-random numbers

# Importing random module
import random

# Using randint() function helps us to generate numbers between the mentioned range
# Ex: random.randint(1,10) -- Will give us a random number from 1 to 10, both 1 and 10 are included
random_guess = random.randint(0,1)

# Simple if-else conditional to print the result based on the random integer generated
if random_guess == 1:
    print("Heads")
else:
    print("Tails")