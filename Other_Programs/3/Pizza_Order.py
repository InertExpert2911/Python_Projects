# Welcome customer
print("Welcome to Python Pizza Deliveries!")

# Inputs from the customer
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Variable to store price of the items
price_to_pay = 0

# Adding the price as per customer's choice
if size == 'S':
    price_to_pay += 15
elif size == 'M':
    price_to_pay += 20
else:
    price_to_pay += 25
    
# Getting choice of the customer and adding the amount to the bill
if add_pepperoni == 'Y':
    if size == 'S':
        price_to_pay += 2
    else:
        price_to_pay += 3

# Adding $1, if the customer needs extra cheese
if extra_cheese == 'Y':
    price_to_pay += 1

# Printing total price
print(f"Your final bill is: ${price_to_pay}.")


