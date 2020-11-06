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
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.8
    }
        }
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """checks whether the machine has sufficient resources to make drink"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * .25
    total += int(input("how many dimes?: ")) * .10
    total += int(input("how many nickels?:")) * .05
    total += int(input("how many pennies?:")) * .01
    return total

def make_coffee(drink):
    """Takes drink order and subtracts ingredient cost from the resources of the machine"""
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]

is_on = True

while is_on:
    choice = input("What would you like to drink (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Powering down...")
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            print(f"Drink cost is: {drink['cost']}")
            payment = process_coins()
            if payment >= drink['cost']:
                print(f"Your change is ${round(payment-drink['cost'],2)}. ")
                profit += drink['cost']
                make_coffee(drink)
                print("Enjoy your drink, and have a nice day!")
            else:
                print("Sorry, you didn't insert enough money. Money Refunded")




