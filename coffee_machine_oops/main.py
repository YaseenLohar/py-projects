from tabnanny import check

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def give_coffee():
    rep = CoffeeMaker()
    pay = MoneyMachine()

    while True:
        #TODO.1 prompt the user
        choice = input("What would you like to order? ")
        #TODO.2 off the machine for maintenance
        if choice == "off":
            print("turning off coffee machine")
            break

        #TODO.3 printing the report

        if choice == "report":
            rep.report()
            continue


        #TODO.4 check if resources are sufficient

        if choice == "latte" or choice == "espresso" or choice == "cappuccino":
            item= Menu()
            req= item.find_drink(choice)  #required drink, menuitem object return

        if str(rep.is_resource_sufficient(req)) == "False":
            break

        #TODO.5 process coins
        pay.make_payment(req.cost)

        #TODO.6 make coffee
        rep.make_coffee(req)

        #TODO.7 check profit
        pay.report()

give_coffee()
