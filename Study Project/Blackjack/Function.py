# Function

def your(your_card, cards, get_another_card, random):
    len_card = len(your_card)
    if get_another_card == "":
        while len_card != 2:
            your_card.append(random.choice(cards))
            len_card = len(your_card)
    elif get_another_card == "y":
        your_card.append(random.choice(cards))
    elif get_another_card == "n":
        pass
    return your_card

def computer(computer_card, cards, get_another_card, random):
    len_card = len(computer_card)
    if get_another_card == "":
        while len_card != 2:
            computer_card.append(random.choice(cards))
            len_card = len(computer_card)
    elif get_another_card == "y":
        computer_card.append(random.choice(cards))
    elif get_another_card == "n":
        pass
    return computer_card

def get_another(get_another_card):
    get_another_card = "" 
    while get_another_card != "y" and get_another_card != "n":
        get_another_card = input(f"Type 'y' to get another card, type 'n' to pass : ").lower()
    return get_another_card

def checking_card(card, score, result):
    score = 0
    result = ""
    for numb in card:
            score += numb
            if score > 21:
                len_card = len(card)
                for numb in range(0, len_card - 1):
                    if card[numb] == 11:
                        card[numb] = 1
                score -= 21
                result = "End"
    return card, score, result

# def final_your_card(user_result, get_another_card, your_card, your_final_card, winner, play):
#     your_final_card = 0
#     if get_another_card == "y":
#         for numb in your_card:
#             your_final_card += numb
#             if your_final_card > 21:
#                 len_card = len(your_card)
#                 for numb in range(0, len_card - 1):
#                     if your_card[numb] == 11:
#                         your_card[numb] = 1
#                 your_final_card -= 21
#                 # sum(cards)
#                 user_result = "End"
#     elif get_another_card == "n":
#         for numb in your_card:
#             your_final_card += numb
#             print(your_final_card)
#             if your_final_card > 21:
#                 len_card = len(your_card)
#                 for numb in range(0, len_card - 1):
#                     if your_card[numb] == 11:
#                         your_card[numb] = 1
#                 your_final_card -= 21
#                 # sum(cards)
#                 user_result = "End"
#     return user_result, play, your_final_card

# def final_computer_card(computer_result, get_another_card, computer_card, computer_final_card, winner, play):
#     computer_final_card = 0
#     if get_another_card == "y":
#         for numb in computer_card:
#             computer_final_card += numb
#             if computer_final_card > 21:
#                 len_card = len(computer_card)
#                 for numb in range(0, len_card - 1):
#                     if computer_card[numb] == 11:
#                         computer_card[numb] = 1
#                 computer_final_card -= 21
#                 # sum(cards)
#                 computer_result = "End"
#     elif get_another_card == "n":
#         for numb in computer_card:
#             computer_final_card += numb
#             print(computer_final_card)
#             if computer_final_card > 21:
#                 len_card = len(computer_card)
#                 for numb in range(0, len_card - 1):
#                     if computer_card[numb] == 11:
#                         computer_card[numb] = 1
#                 computer_final_card -= 21
#                 # sum(cards)
#                 computer_result = "End"
#     return computer_result, play, computer_final_card
             
def result_check_card(winner, play, user_result, computer_result):
    if user_result == "End" or computer_result == "End":
        if user_result == "End" and computer_result == "End":
            winner = "DRAW. NO ONE WIN !!!"
            play = "n"
        elif user_result == "End":
            winner = "Computer Win !!!"
            play = "n"
        elif computer_result == "End":
            winner = "You Win !!!"
            play = "n"
        else:
            pass
    return winner, play

def final_card(get_another_card, your_final_card, computer_final_card, winner, play):  
    if get_another_card == "n":
        if your_final_card > computer_final_card:
            winner = "You Win !!!"
            play = "n"
        elif computer_final_card > your_final_card:
            winner = "Computer Win !!!"
            play = "n"
        elif your_final_card == computer_final_card:
            winner = "DRAW. NO ONE WIN !!!"
            play = "n"
        else:
            pass
    return winner, play
            