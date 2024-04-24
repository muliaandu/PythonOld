# Module.
from Menu import *
import os

os.system("cls")
# TODO: 1. print

# Welcome Message.
print(f"Welcome to The Coffee Machine.")

# Variable.
running = True


# Function.
def coins():
    '''$1 = 100 pennie, 20 nickels, 10 dimes,4 quarter'''
    print(f"Please insert coins.")
    quarter = float(input(f"How many quarters: "))  * 0.25
    dime = float(input(f"How many dimes: ")) * 0.1
    nickle = float(input(f"How many nickles: ")) * 0.05
    pennie = float(input(f"How many pennies: ")) * 0.01
    money = quarter + dime + pennie + nickle
    return money

def reports(order):
    ingredients = MENU[order]["ingredients"]
    cost = MENU[order]["cost"]
    return ingredients, cost

def resource(resources):
    water_re = resources["water"]
    milk_re = resources["milk"]
    coffee_re = resources["coffee"]
    money_re = resources["money"]
    return water_re, milk_re, coffee_re, money_re

# def update(resources, menu):
#     resources
    

# Printout
while running is True:
    order = ""
    while order != "espresso" and order != "latte" and order != "cappuccino" and order != "cancel":
        order = input(f"What would you like? (Espresso/Latte/Cappucino/Cancel): ").lower()
        stock = resource(resources)
        if order == "espresso":
            menu = reports(order)
            if stock[0] < menu[0]["water"]:
                print(f"Sorry that's not enough water.")
            elif stock[2] < menu[0]["coffee"]:
                print(f"Sorry that's not enough coffee.")
            else:
                coin = coins()
                if menu[1] > coin:
                    print(f"Sorry that's not enough money. Money refunded.")
                else:
                    resources["water"] = stock[0] - menu[0]["water"]
                    resources["coffee"] = stock[2] - menu[0]["coffee"]
                    resources["money"] = stock[3] + menu[1]
                    change = coin - menu[1]
                    print(f"Here is your ${change:.2f} change from your ${coin} and your latte ☕ Enjoy")
            
        elif order == "latte":
            menu = reports(order)
            if stock[0] < menu[0]["water"]:
                print(f"Sorry that's not enough water.")
            elif stock[1] < menu[0]["milk"]:
                print(f"Sorry that's not enough milk.")
            elif stock[2] < menu[0]["coffee"]:
                print(f"Sorry that's not enough coffee.")
            else:
                coin = coins()
                if menu[1] > coin:
                    print(f"Sorry that's not enough money. Money refunded.")
                else:
                    resources["water"] = stock[0] - menu[0]["water"]
                    resources["milk"] = stock[1] - menu[0]["milk"]
                    resources["coffee"] = stock[2] - menu[0]["coffee"]
                    resources["money"] = stock[3] + menu[1]
                    change = coin - menu[1]    
                    print(f"Here is your ${change:.2f} change from your ${coin} and your latte ☕ Enjoy")

        elif order == "cappuccino":
            menu = reports(order)
            if stock[0] < menu[0]["water"]:
                print(f"Sorry that's not enough water.")
            elif stock[1] < menu[0]["milk"]:
                print(f"Sorry that's not enough milk.")
            elif stock[2] < menu[0]["coffee"]:
                print(f"Sorry that's not enough coffee.")
            else:
                coin = coins()
                if menu[1] > coin:
                    print(f"Sorry that's not enough money. Money refunded.")
                else:
                    resources["water"] = stock[0] - menu[0]["water"]
                    resources["milk"] = stock[1] - menu[0]["milk"]
                    resources["coffee"] = stock[2] - menu[0]["coffee"]
                    resources["money"] = stock[3] + menu[1]
                    change = coin - menu[1]
                    print(f"Here is your ${change:.2f} change from your ${coin} and your latte ☕ Enjoy")

        elif order == "report":
            print(f"Water: {stock[0]}ml")
            print(f"Milk: {stock[1]}ml")
            print(f"Coffee: {stock[2]}g")
            print(f"Money: ${stock[3]}")
        elif order == "cancel":
            running = False

        