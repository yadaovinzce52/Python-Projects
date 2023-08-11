from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
register = MoneyMachine()


def reports():
    coffee_maker.report()
    register.report()


while True:
    choice = input(f'What would you like? ({menu.get_items()}): ').lower()
    if choice == 'off':
        break
    elif choice == 'report':
        reports()
    elif choice in menu.get_items().split('/'):
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if register.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
