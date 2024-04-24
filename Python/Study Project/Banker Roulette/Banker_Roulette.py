# Importing the Module
import random
# Create an empty list
list_of_name = []
#Create number the name
total_name = int(input(f"Please input how much name will join : "))
number = 0
# Ask for name.
for x in range(total_name):
    name = input(f"Please input the name : ")
    # Move the name into a list.
    list_of_name.append(name)
else:
    random_number = random.randint(0, len(list_of_name) - 1)
    # Print out the result.
    print(f"{list_of_name[random_number]} is going to buy the meal today!")