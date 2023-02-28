# Welcome print statement
print("Welcome to the tip calculator!")

# Declared variables to store user inputs and convert the data type to suit our need
bill_amount = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15 percent? "))
total_people = int(input("How many people to split the bill? "))

# (1 + tip_percentage / 100) => We are doing this to add the tip amount directly to the bill
# Ex: Each person should pay (150.00 / 5) * 1.12 = 33.6
bill_amount_to_pay = (bill_amount / total_people) * (1 + tip_percentage / 100)

# SOLUTION-1: Rounding-off to 2 decimal places
# EX: (number, number_of_digits)
# print(f"Each person should pay: ${round(bill_amount_to_pay, 2)}")


# SOLUTION-2: Using format(num, ".2f") to format the amount to 2 decimal digits
rounded_off_amount_to_pay = format(bill_amount_to_pay, ".2f")

# Printing the final result in an  f-string
print(f"Each person should pay: ${rounded_off_amount_to_pay}")