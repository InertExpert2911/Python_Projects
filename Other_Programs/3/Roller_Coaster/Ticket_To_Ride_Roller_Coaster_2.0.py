# Welcome text
print("Welcome to the roller coaster ticket counter!")

# User input
user_height = int(input("Please tell us your height in cm: "))

# Variable to hold bill
bill = 0

# Conditionals if, else and elif
if user_height >= 120:

    print("You can ride the roller coaster, yay!!")
    
    # Input
    user_age = int(input("Enter your age: "))

    # Nested conditionals, if case inside an if case
    # Only one condition is run, so bill variable would hold only one value (5 or 7 or 12)
    if user_age < 12:
        bill = 5
        print("Children tickets costs $5.")
    # elif -- can be used to check extra conditions in conditionals along with an if
    elif user_age <= 18:
        bill = 7
        print("Teenager ticket costs $7.")
    else:
        bill = 12
        print("Adult ticket costs $12.")

    # Input
    wants_photos = input("Do you want a photo taken during your ride? Y or N: ")
    
    # Check if the user needs photos, if yes them add $3 to their bill
    if wants_photos == 'Y':
        bill += 3
    # No need of an else, because if user answers 'N', we don't have to do anything to bill
    
    # Printing total bill amount
    print(f"Your total bill is ${bill}, enjoy the ride!!")
    
else:
    print("Sorry, you can't ride the roller coaster right now.")