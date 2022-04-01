
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(start_text, shift_amount, direction_of_message):
    encrypted_alphabet = alphabet * (shift_amount + 1)
    encrypted_text = []
    if direction_of_message == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = encrypted_alphabet.index(char)
            new_position = position + shift_amount
            letter_encrypted = encrypted_alphabet[new_position]
            encrypted_text.append(letter_encrypted)
        else:
            encrypted_text.append(char)
    print(f"The {direction_of_message}d text is {''.join(encrypted_text)}")
play = 'yes'
while play == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)
    continue_playing = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if continue_playing == 'yes':
        play = 'yes'
    else:
        play = 'no'
        print("Goodbye!")


 