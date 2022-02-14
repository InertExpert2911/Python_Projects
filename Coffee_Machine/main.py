# GLOBAL VARIABLES.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

MONEY = 0

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(item_ingredients):
    """Returns True when order can be made (sufficient resources), False if ingredients are insufficient."""
    # Looping through each item in ingredients.
    for item in item_ingredients:
        # If more ingredients are needed that the present resources, return False.
        if item_ingredients[item] > RESOURCES[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total monetary value calculated from inserted coins."""
    print("Please insert coins.")
    # Defining a variable and updating it.
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickels? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total


def is_transaction_successful(money_inserted, cost_of_the_drink):
    """Returns True when the transaction is successful, or False if money inserted is insufficient."""
    # Checking if money put in is enough to but the drink user requested.
    if money_inserted >= cost_of_the_drink:
        # Calculating change and returning it to the user.
        change = round(money_inserted - cost_of_the_drink, 2)
        print(f"Here is you change of ${change}.")
        # Getting MONEY.
        global MONEY
        # Updating MONEY with the cost of the drink.
        MONEY += cost_of_the_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, item_ingredients):
    """Deduct the required ingredients from the available resources."""
    for item in item_ingredients:
        # Deducting the resources based on item ingredients.
        RESOURCES[item] -= item_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


# Flag to control while loop.
machine_is_on = True

while machine_is_on:
    # user input.
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # To switch off the machine for maintenance.
    if user_choice == "off":
        machine_is_on = False
        # exit() --> This will work the same as the above flag.

    # To understand what resources are left.
    elif user_choice == "report":
        print(
            f" Water: {RESOURCES['water']}ml \n Milk: {RESOURCES['milk']}ml \n Coffee: {RESOURCES['coffee']}g \n Money: {MONEY}"
        )
    else:
        user_drink = MENU[user_choice]
        # print(user_drink)

        # Checking we have enough resources.
        if check_resources(user_drink["ingredients"]):
            # The value of money inserted is stored in payment.
            payment = process_coins()

            # If transaction is successful give user the drink and deduct the resources based on user's choice.
            if is_transaction_successful(payment, user_drink["cost"]):
                make_coffee(user_choice, user_drink["ingredients"])


# EXTRA FUNCTIONALITY:

# 1. Print MONEY only when there is money.
# 2. Automatically exit out of while loop when we don't have enough resources.
