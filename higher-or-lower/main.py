from data import data
from art import logo, vs
import random
import os

    

def compare(A, B):
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if A["follower_count"] > B["follower_count"] and guess == 'a':
        return True
    elif A["follower_count"] > B["follower_count"] and guess == 'b':
        return False
    elif A["follower_count"] < B["follower_count"] and guess == 'a':
        return False
    elif A["follower_count"] < B["follower_count"] and guess == 'b':
        return True
    else:
        return False

def play():
    score = 0 
    should_continue = True 
    person1 = random.choice(data)
    print(logo)
    while should_continue:
        name1 = person1["name"]
        description1 = person1["description"]
        country1 = person1["country"]
        print(f"Compare A: {name1}, a {description1}, from {country1}!")
        person2 = random.choice(data)
        while person2 == person1:
            person2 = random.choice(data)
        name2 = person2["name"]
        description2 = person2["description"]
        country2 = person2["country"]
        print(vs)
        print(f"Against B: {name2}, a {description2}, from {country2}!")
        if compare(person1, person2):
            person1 = person2
            score += 1
            os.system('cls')
            print(logo)
            print(f"You're right! Current score: {score}!")
        else: 
            should_continue = False
            os.system('cls')
            print(logo)
            print(f"Sorry that's wrong. Final score: {score}.")
play()