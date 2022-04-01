print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = (input("You're at a crossroad, where do you want to go? Type 'left' or 'right'\n")).lower()
if choice1 == 'left':
    choice2 = (input("There is a big lake, do you want to swim or wait? Type 'swim' or 'wait'\n")).lower()
    if choice2 == 'wait':
        choice3 = (input("You arrive at an island and there are three paths, one is red, one is blue, and one is yellow! Choose 'red', 'blue', or 'yellow'!\n")).lower()
        if choice3 == 'red':
            print("Game Over! Red is mad sussss...")
        elif choice3 == 'blue':
            print("You found my dick, you win!")
        elif choice3 == 'yellow':
            print("Game Over! A giant pisses on you and you drown!")
        else:
            print("Game Over! It was not even an option dumbass...")
    else:
        print("Game Over! You drown!")

else:
    print("Gameover! You fell into a hole filled with monkeys who are very hangry!")
    


