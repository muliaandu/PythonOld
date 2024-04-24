# Module.
import random
import Hangman_art 
import Hangman_live_level 
import Animals_name 

# Welcome Message.
print(f"{Hangman_art.hangman_art}")
print(f"Welcome to Guess The Name of Animal Game.")

# Variable.
word_list = Animals_name.animal_name.lower().split()
guess = ""
chosen_word = ""
guesses = ""
final_guess = ""
final_chosen_word = []
live = 6
hangman = 0

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list).lower()
for char in chosen_word:
    final_chosen_word += char
x = len(chosen_word)
guesses = ("_ " * x).split()

# TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
while guesses != final_chosen_word and live != 0:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    print(f"Your live : {live}")
    print(f"{Hangman_live_level.HANGMANPICS[hangman]}")
    print(" ".join(guesses))
    guess = input(f"\nGuess a letter of animal name : ").lower()
    # Looping to get check a single letter and if right, letter will be replace the "_".
    for letter in range(0, x):
    # for letter in chosen_word:
        # if letter == guess:
        if guess == chosen_word[letter]:
            # print(f"Right")
            guesses[letter] = guess
        else:
            pass
            # print(f"Wrong")
    # Checking the letter of guess in the chosen_word. same like for loop but this one not looping.
    if guess not in chosen_word:
        live -= 1
        hangman += 1
        print(f"You are wrong. Your life remaining {live}")
    if guess in guesses:
        print(f"You have been guess this letter '{guess.upper()}' before.")
else:
    pass
# For looping to joining the list become a string. otherwise u can use other method using .join like below.
final_guess = "".join(guesses)
# for x in range(0, x):
#     final_guess += guesses[x]
if guesses == final_chosen_word and live != 0:
    print(f"\nThe Final Name of Animal is {final_guess.upper()}")
    print(f"Corangtulation, You are WIN !!!\n")
else :
    final_guess = "".join(chosen_word)
    print(f"\nThe Final Name of Animal is {final_guess.upper()}")
    print(f"You are LOSE !!!")
