bprint("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

bill_and_tip = bill * (1 + tip / 100)

people = int(input("How many people to split the bill? "))

amt_per_person = bill_and_tip / people

round_amt = round(amt_per_person, 2)

formated_amt = "{:.2f}".format(amt_per_person)

print(f"Each person should pay: ${formated_amt}")

