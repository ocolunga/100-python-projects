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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    """Prints the current resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    return None


def check_resources(drink: dict):
    """Checks if there are enough resources to make the selection"""
    for item in drink["ingredients"]:
        if resources[item] < drink["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Processes the coins inserted by the user"""
    print("Please insert coins.")
    input_quarters = int(input("How many quarters?: "))
    input_dimes = int(input("How many dimes?: "))
    input_nickels = int(input("How many nickels?: "))
    input_pennies = int(input("How many pennies?: "))
    total = (
        input_quarters * 0.25
        + input_dimes * 0.1
        + input_nickels * 0.05
        + input_pennies * 0.01
    )
    return total


def check_transaction(total: float, drink: dict):
    """Checks if the transaction is successful"""
    cost = drink["cost"]
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:  # Simplified to else, covering both equal and greater than cost cases
        if total > cost:
            change = round(total - cost, 2)  # Fix: Round change to 2 decimal places
            print(f"Here is ${change} in change.")
        return True


def add_profit(drink: dict):
    """Adds the profit to the resources"""
    resources["money"] += drink["cost"]


def reduct_resources(drink: dict):
    """Reducts the resources used to make the selection"""
    for item, amount in drink[
        "ingredients"
    ].items():  # Fix: Iterate over items and amounts
        resources[item] -= amount


is_on = True

while is_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "off":
        print("Turning off the machine")
        is_on = False
    elif selection == "report":
        report()
        continue
    elif selection not in MENU:
        print("Invalid selection")
        continue
    else:
        drink = MENU[selection]
        if check_resources(drink):
            total = process_coins()
            if check_transaction(total, drink):
                add_profit(drink)
                print(f"Here is your {selection}. Enjoy!")
                reduct_resources(drink)
