print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

tip_cal = total_bill * (1 + tip / 100)

people = int(input("How many people to split the bill? "))

total_amt = tip_cal / people

final_amt = round(total_amt, 2)

final_amt = "{:.2f}".format(total_amt)

print(f"Each person should pay: ${final_amt}")

#https://replit.com/@TharunReddy5/TipCalculator#main.py