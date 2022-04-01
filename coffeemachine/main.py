
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def report():
    for resource, quantity in resources.items():
        print(resource, ': ', quantity)


def coins(coffee_chosen):
    try:
        ingredient = MENU[coffee_chosen]["ingredients"]
        for key in ingredient:
            if ingredient[key] > resources[key]:
                print(f"Sorry not enough {key}!")
                return False
            else:
                print("Please insert coins. ")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                Total_cash = round(float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)), 2)
                cash_required = MENU[coffee_chosen]["cost"]
                if Total_cash > cash_required:
                    cash_returned = round(Total_cash - cash_required, 2)
                    print(f"Here is your change {cash_returned}$")
                    resources["coffee"] -= ingredient["coffee"]
                    resources["milk"] -= ingredient["milk"]
                    resources["water"] -= ingredient["water"]
                    return True
                elif Total_cash == cash_required:
                    print("There is no change!")
                    resources["coffee"] -= ingredient["coffee"]
                    resources["milk"] -= ingredient["milk"]
                    resources["water"] -= ingredient["water"]
                    return True
                else:
                    print("Sorry, that's not enough money. Money refunded.")
                    Total_cash = 0
                    return False
    except:
        print("That is not money")
        return False      


def coffee():
    service = True
    while service:
        coffee_choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_choice == 'off':
            service = False
        elif coffee_choice == 'refill':
            resources["water"] = 300
            resources["milk"] = 200
            resources["coffee"] = 100
            print("The machine has been refilled!")
        elif coffee_choice == 'espresso':
            if coins("espresso"):
                print("Here is your espresso! Enjoy ☕")
        elif coffee_choice == 'latte':
            if coins("latte"):
                print("Here is your latte! Enjoy ☕")
        elif coffee_choice == 'cappuccino':
            if coins("cappuccino"):
                print("Here is your cappuccino! Enjoy ☕")
        elif coffee_choice == 'report':
            report()
        else:
            print("Invalid Command!")
            coffee()    


coffee()

