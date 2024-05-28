# Define a dictionary to store the menu items with their ingredients and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,  # amount of water required for an espresso
            "coffee": 18,  # amount of coffee required for an espresso
        },
        "cost": 1.5,  # cost of an espresso
    },
    "latte": {
        "ingredients": {
            "water": 200,  # amount of water required for a latte
            "milk": 150,  # amount of milk required for a latte
            "coffee": 24,  # amount of coffee required for a latte
        },
        "cost": 2.5,  # cost of a latte
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,  # amount of water required for a cappuccino
            "milk": 100,  # amount of milk required for a cappuccino
            "coffee": 24,  # amount of coffee required for a cappuccino
        },
        "cost": 3.0,  # cost of a cappuccino
    }
}

# Initialize resources available in the machine
resources = {
    "water": 300,  # initial amount of water in the machine
    "milk": 200,  # initial amount of milk in the machine
    "coffee": 100,  # initial amount of coffee in the machine
}
Money = 0  # initial amount of money in the machine


def is_resourse_sufficient(order_ingredients):
    """
    Check if the resources are sufficient to make the drink.
    This function takes the ingredients required for the drink as input and checks if the machine has enough resources.
    If not, it prints an error message and returns False. Otherwise, it returns True.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins(drink_cost):
    """
    Process the coins inserted by the user to pay for the drink.
    This function takes the cost of the drink as input and prompts the user to insert coins.
    It returns the total amount of money inserted.
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """
    Check if the money inserted is sufficient to buy the drink.
    This function takes the amount of money inserted and the cost of the drink as input.
    If the money is sufficient, it calculates the change and updates the machine's money. Otherwise, it refunds the money.
    """
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global Money
        Money += drink_cost
    elif money_recieved < drink_cost:
        print("Sorry that's not enough money. Money refunded.")


def Make_coffee(drink_name, order_ingredients):
    """
    Make the coffee by deducting the ingredients from the resources.
    This function takes the name of the drink and its ingredients as input.
    It updates the resources and prints a success message.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy")


def refill():
    """
    Refill the resources in the machine.
    This function resets the resources to their initial values.
    """
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100


is_on = True  # flag to indicate if the machine is on

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False  # turn off the machine
    elif choice == "report":
        # print the current resources and money
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${Money}")
    elif choice == "refill":
        refill()  # refill
