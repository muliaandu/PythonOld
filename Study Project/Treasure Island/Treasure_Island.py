# Welcome message
print(f"""Welcome to Treasure Island.
      
Your mission is to find the treasure.\n""")

# Game 1
first = input(f"You're at a cross road. Where do you want to go? (left or right). ")
if first.lower() == "left":
    # game 2
    second = input(f"""You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boar. Type "swim" to swim across.""")
    if second.lower() == "wait":
        # game 3
        third = input(f"""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? (red or yellow or blue).""")
        # Finish the game
        if third.lower() == "yellow":
            print(f"Congratulation. You WIN !!!!")
        else:
            print(f"You enter a room of beasts. Game Over.")
    else:
        print(f"You killed by Killer Fish. Game Over.")
else:
    print(f"You enter a territory of beasts. Game Over.")