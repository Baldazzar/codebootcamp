from art import logo
import os

print(logo)

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
    "**": exponent,
}
def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2) 

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation or anything else to exit: ") 
        if continue_calc == "y":
            num1 = answer
        elif continue_calc  == "n":
            should_continue = False
            os.system('cls')
            print(logo)
            calculator()
        else:
            return

calculator()