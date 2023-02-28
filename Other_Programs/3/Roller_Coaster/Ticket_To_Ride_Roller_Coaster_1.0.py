print("Welcome to the roller coaster ticket counter!")

# User input
user_height = int(input("Please tell us your height in cm: "))

# Conditionals if, else
if user_height >= 120:

    print("You can ride the roller coaster, yay!!")
    user_age = int(input("Enter your age: "))

    # Nested conditionals, if case inside an if case
    if user_age < 12:
        print("Your ticket costs $5.")
    # elif -- can be used to check extra conditions in conditionals along with an if
    elif user_age <= 18:
        print("Your ticket costs $7.")
    else:
        print("Your ticket costs $12.")

else:
    print("Sorry, you can't ride the roller coaster right now.")
