import random

# TESTING CODE
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# This initializes a random number generator.
# To generate a new random sequence, a seed must be set depending on the current system time.
# random.seed() sets the seed for random number generation.
# TESTING CODE 

rand_num = random.randint(0,1)

if rand_num == 0:
    print("Tails")
else:
    print("Heads")