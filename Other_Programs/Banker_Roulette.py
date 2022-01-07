import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
# .split() --> Converts a string into a list based on the specified special characters.
names = names_string.split(", ")

length_of_list = len(names)

# Random Number
# length_of_list - 1 --> We are using this because of INDEXING IN PYTHON.
random_num = random.randint(0, length_of_list - 1) 

# Indexing
random_name = names[random_num] 
print(f"{random_name} is going to buy the meal today!")
