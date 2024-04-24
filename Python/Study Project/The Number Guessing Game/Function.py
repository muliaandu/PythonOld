def guessing(guess, attempts, game_on):
    if attempts != 0 :
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input(f"Make a guess : "))
        attempts -= 1
    elif attempts == 0:
        game_on = False
        print(f"\nYou've run out of guesses, you lose.")
    return guess, attempts, game_on

def random_number(random, random_numb):
    random_numb = random.randint(1, 101)
    return random_numb

def choose_difficulty(difficulty, attempts):
    print(f"\nI'm thinking of a number between 1 and 100.")
    while difficulty != "easy" and difficulty != "hard" :
        difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    return difficulty, attempts

def checking_guesses(guess, random_numb, game_on, result):
    if game_on == True:
        if guess > random_numb:
            print(f"Too high.")
            print(f"Guess again. ")
        elif guess < random_numb:
            print(f"Too low.")
            print(f"Guess again. ")
        elif guess == random_numb:
            game_on = False
            result = "Win"
            print(f"\nWou are {result} in this match.")
    else:
        pass
    return game_on, result