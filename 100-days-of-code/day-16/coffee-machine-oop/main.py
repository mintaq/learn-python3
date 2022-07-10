from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

profit = 0
is_machine_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_machine_on:
    order = input("What is your order (latte | espresso | cappuccino): ")
    if order == "off":
        is_machine_on = False
        print("Turning off")
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
