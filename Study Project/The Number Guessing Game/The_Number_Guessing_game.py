import os
os.system("cls")

# Welcome Message.
print(f"Welcome to The Number Guessing Game !")

# Module
from Variable import *
from Function import *
import random
import os

choose = choose_difficulty(difficulty = difficulty, attempts = attempts)
difficulty = choose[0]
attempts = choose[1]
random_numb = random_number(random = random, random_numb = random_numb)
print(random_numb)

while game_on == True:
    result_guess = guessing(guess = guess, attempts = attempts, game_on = game_on)
    guess = result_guess[0]
    attempts = result_guess[1]
    game_on = result_guess[2]
    check = checking_guesses(guess = guess, random_numb = random_numb, game_on = game_on, result = result)
    game_on = check[0]
    result = check[1]