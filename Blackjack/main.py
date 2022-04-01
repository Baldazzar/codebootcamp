from art import logo
import random
import os
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

def pick_card_player():
    card1 = random.choice(cards)
    user_cards.append(card1) 
    card2 = random.choice(cards)
    user_cards.append(card2)
    print(f"Your cards are: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card is: {dealer_cards[0]}")
    should_continue = True
    while should_continue:
        Ace = 11
        if Ace in user_cards and sum(user_cards) > 21:
            user_cards[user_cards.index(Ace)] = 1 
            time.sleep(1)
            print("Your Ace(11) will be changed to 1, since you're score is above 21!")
            time.sleep(1)
            print(f"Your cards are: {user_cards}, current score: {sum(user_cards)}")
        else:
            if sum(user_cards) > 21:
                should_continue = False
                print("You Lose!")
                return

            if sum(user_cards) == 21:
                should_continue = False
                print(f"Computer's cards: {dealer_cards}, Computer's score: {sum(dealer_cards)}")
                return check_winner()
            else:
                pick_another_card = input("Type 'y' to pick another card or 'n' to pass.\n")
                if pick_another_card == 'y':
                    card3 = random.choice(cards)
                    user_cards.append(card3)
                    print(f"Your cards are: {user_cards}, current score: {sum(user_cards)}")
                else:
                    should_continue = False
                    print(f"Computer's cards: {dealer_cards}, Computer's score: {sum(dealer_cards)}")
                    return check_winner()

def pick_card_dealer():
    card1 = random.choice(cards)
    dealer_cards.append(card1) 
    card2 = random.choice(cards)
    dealer_cards.append(card2)
    while sum(dealer_cards) < 17:
        Ace = 11
        if Ace in user_cards and sum(dealer_cards) > 21:
            user_cards[user_cards.index(Ace)] = 1
        else: 
            card3 = random.choice(cards)
            dealer_cards.append(card3)
    return dealer_cards

def check_winner():
    if sum(user_cards) == sum(dealer_cards):
        return print("Draw!")
    if sum(user_cards) > sum(dealer_cards) and sum(user_cards) <= 21:
        return print("You win!")
    if sum(user_cards) < sum(dealer_cards) and sum(dealer_cards) <= 21:
        return print("You lose!")
    else:
        return print("You win!")

def clear_list():
    user_cards.clear()
    dealer_cards.clear()

def play():
    print(logo)
    continue_playing = True
    while continue_playing:
        question = input("Do you want to play a game of blackjack? 'y' or 'n'?\n").lower()
        os.system('cls')
        if question == 'y':
            pick_card_dealer()
            pick_card_player()
            clear_list()

        else:
            continue_playing = False
            print("Goodbye!")
    
play()


