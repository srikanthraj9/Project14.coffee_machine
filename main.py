from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
coffee = True
while coffee:
    user_choice = input("which one you want latte/espresso/cappuccino and do want see resource please click 'r' \n").lower()
    if user_choice == "r":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        coffee = False
        print("see you latter")
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(money_machine.make_payment(drink.cost))
            coffee_maker.make_coffee(drink)




