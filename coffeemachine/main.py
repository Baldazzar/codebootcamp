
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


def check_ressources(coffee_chosen):
    ingredient = MENU[coffee_chosen]["ingredients"]
    for key in ingredient:
        if ingredient[key] > resources[key]:
            print(f"Sorry not enough {key}!")
            return False
    resources["coffee"] -= ingredient["coffee"]
    resources["milk"] -= ingredient["milk"]
    resources["water"] -= ingredient["water"]
    return True                



def coins(coffee_chosen):
    print("Please insert coins. ")
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        Total_cash = round(float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)), 2)
        cash_required = MENU[coffee_chosen]["cost"]
        if Total_cash > cash_required:
            cash_returned = round(Total_cash - cash_required, 2)
            print(f"Here is your change {cash_returned}$")
            return True
        elif Total_cash == cash_required:
            print("There is no change!")
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
        elif coffee_choice == 'espresso':
            if check_ressources("espresso") and coins("espresso"):
                print("Here is your espresso! Enjoy ☕")
        elif coffee_choice == 'latte':
            if check_ressources("latte") and coins("latte"):
                print("Here is your latte! Enjoy ☕")
        elif coffee_choice == 'cappuccino':
            if check_ressources("cappuccino") and coins("cappuccino"):
                print("Here is your cappuccino! Enjoy ☕")
        elif coffee_choice == 'report':
            report()
        else:
            print("Invalid Command!")
            coffee()    


coffee()

