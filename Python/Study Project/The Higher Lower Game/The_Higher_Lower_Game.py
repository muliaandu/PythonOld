# Module.
import random
from Data import *
from Art import *
import os

# Welcome Message.
print(f"Welcome to The Higher Lower Game.")
print(logo)

# Variable.
game_on = True
random_numb = 0
name_a = ""
name_b = ""
description_a = ""
description_b = ""
country_a = ""
country_b = ""
follower_count_a = 0
follower_count_b = 0
score = 0

def database(data):
    random_numb = random.randint(0, len(data) - 1)
    name = data[random_numb]["name"]
    follower_count = data[random_numb]["follower_count"]
    description = data[random_numb]["description"]
    country = data[random_numb]["country"]
    return name, follower_count, description, country



while game_on is True:
    result = database(data)
    name_a = result[0]
    follower_count_a = result[1]
    description_a = result[2]
    country_a = result[3]

    result = database(data)
    name_b = result[0]
    follower_count_b = result[1]
    description_b = result[2]
    country_b = result[3]
    
    if name_a == name_b:
        result = database(data)
        name_b = result[0]
        follower_count_b = result[1]
        description_b = result[2]
        country_b = result[3]

    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    print(vs)
    print(f"Against B: {name_b}, a {description_b}, from {country_b} \n")

    compare = ""
    while compare != "a" and compare != "b":
        compare = input(f"Who has more followers? Type 'A' or 'B': ").lower()
    
    os.system("cls")
    print(logo)
    
    if follower_count_a > follower_count_b:
        if compare == "a":
            score += 1
            print(f"You're right! Current score : {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_on = False
    elif follower_count_a < follower_count_b:
        if compare == "b":
            score += 1
            print(f"You're right! Current score : {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_on = False
