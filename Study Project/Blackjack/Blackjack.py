# Import Module.py
from Module import *
os.system("cls")

# Welcome message.
print(f"Welcome to Blackjack game.\n")

# Ask do you want to play Blackjack.
while play != "y" and play != "n":
    play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()

# Logic to response the first input.
while play == "y":
    os.system("cls")

    your_card = your(your_card = your_card, cards = cards, get_another_card = get_another_card, random = random)
    print(f"Your cards : {your_card}")
    check = checking_card(card = your_card, score = your_final_card, result = result)
    user_result = check[2]
    your_final_card = check[1]

    computer_card = computer(computer_card = computer_card, cards = cards, get_another_card = get_another_card, random = random)
    print(f"Computer's first card : [{computer_card[0]}]\n")
    check = checking_card(card = computer_card, score = computer_final_card, result = result)
    computer_result = check[2]
    computer_final_card = check[1]

    result = result_check_card(winner = winner, play = play, user_result = user_result, computer_result = computer_result)
    winner = result[0]
    play = result[1]

    get_another_card = get_another(get_another_card = get_another_card)
    print(get_another_card)

    result = final_card(get_another_card = get_another_card, your_final_card = your_final_card, computer_final_card = computer_final_card, winner = winner, play = play)
    winner = result[0]
    play = result[1]

    # result = final_your_card(user_result = user_result,get_another_card = get_another_card, your_card = your_card, your_final_card = your_final_card, winner = winner, play = play)
    # user_result = result[0]
    # play = result[1]
    # your_final_card = result[2]

    # result = final_computer_card(computer_result = computer_result, get_another_card = get_another_card, computer_card = computer_card, computer_final_card = computer_final_card, winner = winner, play = play)
    # computer_result = result[0]
    # play = result[1]
    # computer_final_card = result[2]

else: 
    os.system("cls")
    print(f"\nYour final hand {your_card} with score {your_final_card}.")
    print(f"Computer's final hand {computer_card} with score {computer_final_card}.")
    print(f"\n{winner}")