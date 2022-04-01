import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
possible_picks = [rock, paper, scissors]
choice_of_player = int(input("Choose what you want to play? Type 0 for Rock, 1 for Paper, or 2 for scissors!\n"))
if choice_of_player > 2:
    print("You lose, you entered an invalid command!")
else:
    choice = possible_picks[choice_of_player]
    computer_choice = random.choice(possible_picks)
    if (choice == rock and computer_choice == scissors) or (choice == paper and computer_choice == rock) or (choice == scissors and computer_choice == paper):
        print(f"You chose:\n {choice}\nYour opponent chose:\n {computer_choice}\n")
        print("You Win!")
    elif choice == computer_choice:
        print(f"You chose:\n {choice}\nYour opponent chose:\n {computer_choice}\n")
        print("Draw!")
    else:
        print(f"You chose:\n {choice}\nYour opponent chose:\n {computer_choice}\n")
        print("You Lose!")

