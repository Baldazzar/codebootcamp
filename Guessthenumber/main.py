import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100! Try to Guess!")
def play():
    number = random.choice(range(1, 101))
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if difficulty == 'easy':
        lives = 10
        print(f"You have {lives} guesses! Good Luck!")
    elif difficulty == 'hard':
        lives = 5
        print(f"You have {lives} guesses! Good Luck!")
    else:
        return print("Invalid Difficulty, Fuck Off")
    while lives != 0:
        try:
            guess = int(input("Enter a number from 1 to 100: "))
            if guess != number:
                lives -= 1
                if guess > number:
                    print(f"Too High! Try Again!\nYou have {lives} guesses remaining!")
                else:
                    print(f"Too Low! Try Again!\nYou have {lives} guesses remaining!")
            else:
                return print(f"You win, the number was {number}")
        except:
            return print("That is not a number you dumbass!")
    return print(f"You are out of guesses, you lose, the number was {number}")

play()
