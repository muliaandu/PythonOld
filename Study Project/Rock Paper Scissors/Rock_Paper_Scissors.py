import random

rock = ("""0
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""1
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""2
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# game_images = [rock, paper, scissors]
# Ask to choose Rock or Paper or Scissors.
# choosed = ""
# while choosed == "":
#     choosed = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))
#     if choosed > 2:
choosed = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))
# Print out the player number.
print(f"You choose {choosed}.")
# print(f"{game_images[choosed]}")
if choosed == 0:
    print(f"{rock}")
elif choosed == 1:
    print(f"{paper}")
else:
    print(f"{scissors}")

# Logic to randomize AI.
game = ["0","1","2"]
ai_choose = int(random.choice(game))
# ai_choose = random.randint(0, 2)
print(f"Computer chose {ai_choose}.")
if ai_choose == 0:
    print(f"{rock}")
elif ai_choose == 1:
    print(f"{paper}")
else:
    print(f"{scissors}")

# Logic about rule the game.
# Rock wins against Scissors.
# Scissors win against Paper.
# Paper win against Rock.
if choosed == 0:
    if ai_choose == 1:
        print(f"YOU LOSE !!!")
    elif ai_choose == 2:
        print(f"YOU WIN !!!")
    else:
        print(f"WA ARE DRAW !!!")
elif choosed == 1:
    if ai_choose == 2:
        print(f"YOU LOSE !!!")
    elif ai_choose == 0:
        print(f"YOU WIN !!!")
    else:
        print(f"WA ARE DRAW !!!")
else:
    if ai_choose == 0:
        print(f"YOU LOSE !!!")
    elif ai_choose == 1:
        print(f"YOU WIN !!!")
    else:
        print(f"WA ARE DRAW !!!")

