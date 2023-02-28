
print("Welcome to the Love Calculator!")

# Inputs
name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")

# Combine the names into a single string
combined_names = name_1 + name_2

# Convert combined string to lowercase with .lower()
lowercase_names = combined_names.lower()

# Counting the occurrences of t, r, u and e letters in both names, with the help of .count('_')
count_of_t = lowercase_names.count('t')
count_of_r = lowercase_names.count('r')
count_of_u = lowercase_names.count('u')
count_of_e = lowercase_names.count('e')

# Total sum of 'true' occurrences
count_of_true = count_of_t + count_of_r + count_of_u + count_of_e

# Counting the occurrences of l, o and v letters in both names
count_of_l = lowercase_names.count('l')
count_of_o = lowercase_names.count('o')
count_of_v = lowercase_names.count('v')

# Total sum of 'love' occurrences
count_of_love = count_of_l + count_of_o + count_of_v + count_of_e

# Converting the ints to a string and concatenating
love_score = int(str(count_of_true) + str(count_of_love))
# print(love_score)

# Checking conditions with love_score and printing results accordingly
if (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
elif (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
else:
    print(f"Your score is {love_score}.")



