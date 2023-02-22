from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_maker = MoneyMachine()

while is_on:
    choices = coffee_menu.get_items()
    order = input(f"What would you like to drink? {choices}: ")
    drink = coffee_menu.find_drink(order)

    #if user input really is a drink
    if drink:
        if coffee_machine.is_resource_sufficient(drink):
            payment = money_maker.make_payment(drink.cost)
            if payment:
                coffee_machine.make_coffee(drink)

    elif order == "report":
        coffee_machine.report()
        money_maker.report()

    else:
        is_on = False





