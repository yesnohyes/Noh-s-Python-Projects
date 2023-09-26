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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

machine_off = False


# TODO: create coffee machine function
def coffee_machine(order):
    # TODO: add in global variables
    global profit
    global resources
    global machine_off
    # TODO: Print resources available if user prompts report
    if user_order == "report":
        water_available = resources["water"]
        milk_available = resources["milk"]
        coffee_available = resources["coffee"]
        print(f"Water: {water_available}ml\nMilk: {milk_available}ml\nCoffee: {coffee_available}g\nMoney: ${profit}")
        return
    # TODO: switch off coffee machine if user prompts off
    elif user_order == "off":
        print("machine turned off")
        machine_off = True
        return

    # TODO: before even moving on to check if user coins are sufficient, check resource availability first
    coffee_chosen = MENU[order]
    # TODO: create variables for amount of resources needed for each order
    water_needed = coffee_chosen["ingredients"]["water"]
    coffee_needed = coffee_chosen["ingredients"]["coffee"]
    if "milk" in coffee_chosen["ingredients"]:
        milk_needed = coffee_chosen["ingredients"]["milk"]
        if milk_needed > resources["milk"]:
            print("Sorry, there is not enough milk.")
            return
    if water_needed > resources["water"]:
        print("Sorry, there is not enough water.")
        return
    elif coffee_needed > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return

    else:

        # TODO: request for coins needed to purchase coffee
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        # TODO: calculate amount of money inserted into machine
        user_money = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies

        # TODO: check if amount of money is enough to purchase the coffee wanted, and dispense coffee if enough
        price_of_coffee = coffee_chosen["cost"]
        if user_money >= price_of_coffee:
            # TODO: if purchase was successful, keep track of profits earned
            user_change = user_money - price_of_coffee
            profit += price_of_coffee
            print(f"Here is ${user_change} in change.\nHere is your {order} ☕. Enjoy!")
            # TODO: additionally if purchase was successful, reduce the resources available according inside the machine
            resources["water"] = resources["water"] - water_needed
            resources["coffee"] = resources["coffee"] - coffee_needed
            if "milk" in coffee_chosen["ingredients"]:
                resources["milk"] = resources["milk"] - milk_needed
        else:
            print("Sorry that's not enough money. Money refunded.")

# TODO: run while loop if machine not off


while not machine_off:
    # TODO: prompt user order
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    coffee_machine(order=user_order)
