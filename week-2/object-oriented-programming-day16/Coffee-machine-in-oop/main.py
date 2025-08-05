# python3 week-2/Coffee-machine-in-oop/main.py

# Secret inputs are "off" to turn the coffie machine off, and "report" to get the machiens info.

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create instances of the objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    off = False
    valid_answer = False
    cost = 0
    item = {}

    while valid_answer == False:
        avalable_items = menu.get_items() #grab items from the menu object
        coffee = input(f"What would you like ({avalable_items}):")

        if coffee != "off" and coffee != "report":
            item = menu.find_drink(coffee)

        if coffee == "off":
            valid_answer = True  
            off = True
        elif coffee == "report":
            coffee_maker.report()
            money_machine.report()
        elif item != None and coffee_maker.is_resource_sufficient(item):
            cost = item.cost
            valid_answer = True
        else:
            print(f"Invalid input, you entered {coffee}, please try again.")

    # if "off" terminate program
    if off == True:
        break

    print(f"Cost: {cost}")
    if money_machine.make_payment(cost):
        coffee_maker.make_coffee(item) 

