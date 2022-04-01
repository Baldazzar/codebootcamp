import random
import os
from hangman_art import stages, logo
from hangman_words import word_list                                      
                                                                    
print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

letter_inputed = []
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess in letter_inputed:
        print(f"{guess} has already been guessed! Try again!")
    else:   
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed letter {guess}, that's not in the word, you lose a life!")
            if lives == 0:
                end_of_game = True 
                print(f"You lose! The word was {chosen_word}!")
    

    print(f"{' '.join(display)}")
    letter_inputed.append(guess)

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
    print(f"Letters guessed: {letter_inputed}")