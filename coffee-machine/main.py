from cmath import pi
from data import MENU, resources, coins_value

total_money = 0

def main():
    is_on = True
    while is_on:
        user_order = input(
            "What would you like? (espresso/latte/cappuccino): ")
        if user_order == "off":
            return print("Turn off!")
        elif user_order == "report":
            print_report()
        else:
            if check_resources_sufficient(user_order):
                money_received = insert_coins()
                if is_transaction_successful(user_order, money_received):
                    deduct_resources(user_order)


def print_report():
    global total_money
    for resource in resources:
        if resource == "water":
            print(f"Water: {resources[resource]}ml")
        if resource == "milk":
            print(f"Milk: {resources[resource]}ml")
        if resource == "coffee":
            print(f"Coffee: {resources[resource]}g")
    print(f"Money: ${total_money}")


def check_resources_sufficient(user_order):
    if user_order not in MENU:
        print("Your choice is not in menu!")
        return False

    picked_drink_ingredients = MENU[user_order]["ingredients"]

    for resource in resources:
        if resource in picked_drink_ingredients:
            if picked_drink_ingredients[resource] > resources[resource]:
                print(f"Sorry there is not enough {resource}")
                return False

    return True


def deduct_resources(user_order):
    picked_drink_ingredients = MENU[user_order]["ingredients"]

    for resource in resources:
        if resource in picked_drink_ingredients:
            resources[resource] -= picked_drink_ingredients[resource]


def insert_coins():
    print("Please insert coins to continue:")
    quarters_number = int(input("Quarters: "))
    dimes_number = int(input("Dimes: "))
    nickles_number = int(input("Nickles: "))
    pennies_number = int(input("Pennies: "))
    total_value = coins_value["quarters"] * quarters_number + coins_value["dimes"] * dimes_number + \
        coins_value["nickles"] * nickles_number + \
        coins_value["pennies"] * pennies_number
    return round(total_value, 2)


def is_transaction_successful(user_order, money_received):
    global total_money
    drink_price = MENU[user_order]["cost"]
    if drink_price <= money_received:
        total_money += drink_price
        change = round(money_received - drink_price, 2)
        print(f"Here is your charge: ${change}")
        return True
    else:
        print(f"You not insert enough coins. Transaction failed!")
        return False


main()
