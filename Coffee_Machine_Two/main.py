from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


machine_is_on = True

while machine_is_on:
    
    # Getting all the coffee options for the user.
    user_options = menu.get_items()
    
    # Getting user input.
    user_choice = input(f"What would you like? ({user_options}): ").lower()

    if user_choice == "off":
        machine_is_on = False

    elif user_choice == "report":
        # Printing the report.
        coffee_maker.report()
        money_machine.report()

    else:
        
        # Finding the user's drink.
        drink = menu.find_drink(user_choice)
        
        # Checking if resources are sufficient and payment is successful.
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
    
            # Making the coffee.
            coffee_maker.make_coffee(drink)
