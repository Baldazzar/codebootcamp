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



def report():
    for resource, quantity in resources.items():
        print(resource, ': ', quantity)


def coins(coffee_chosen):
    print("Please insert coins. ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    Total_cash = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if Total_cash > MENU[coffee_chosen["cost"]]:
        cash_returned = Total_cash - MENU[coffee_chosen["cost"]]
    else:
        print("")
        return False





def espresso():


def coffee():
    service = True
    while service:
        coffee_choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_choice == 'off':
            service = False
        elif coffee_choice == 'espresso':
            if coins("espresso"):
                espresso()
        elif coffee_choice == 'latte':
            if coins("latte"):
                latte()
        elif coffee_choice == 'cappuccino':
            if coins("cappuccino"):
                cappuccino()
        elif coffee_choice == 'report':
            report()
        else:
            print("Invalid Command!")
            coffee()    
