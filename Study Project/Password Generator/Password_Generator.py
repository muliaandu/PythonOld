# Import a module.
import random

# Welcoming Message
print(f"Welcome to the PyPassword Generator.\n")

# Create a variable.
password = []
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = """!"#$%'&\()*+,-./:;<=>?@[]^_{|}~"""
# Ask for how many letter in password.
letter = int(input(f"How many letters would you like in your password? "))
# Ask for how many symbol in password.
symbol = int(input(f"How many symbols would you like? "))
# Ask for how many number in password.
number = int(input(f"How many numbers would you like? "))
# Create a list of numbers from start to ending.
for numb in range(int(letter)):
    password += random.choices(letters)

for numb in range(int(symbol)):
    password += random.choices(symbols)

for numb in range(int(number)):
    password += random.choices(numbers)

pw_1 = ""
for char in password:
    pw_1 += char
print("\n Here is your easy Password : {}.".format(pw_1))

random.shuffle(password)
pw_2 = ""
# pw = "".join(password)
for char in password:
    pw_2 += char
print("\n Here is your hard Password : {}.".format(pw_2))