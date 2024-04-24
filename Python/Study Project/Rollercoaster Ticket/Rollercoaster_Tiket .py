# Print out welcoming message.
print(f"Welcome to the rollercoaster!")
# Asking the height.
height = int(input("What is your height in cm? "))
# Create a logic. Can enter the rides.
if height >= 120:
    print(f"You can ride the Rollercoaster.")
    age = int(input(f"What is your age? "))
    bill = 0
    # Create a logic by age.
    if age < 12:
        print(f"Child ticket is $5.")
        bill += 5
        # photo = input("Do you want photos? (Yes or No).")
        # if photo == "yes" or photo == "Yes":
        #     print(f"Adding $3 for photos.")
        #     total_bill = 5 + 3
        #     print(f"Your total bill is ${total_bill}.")
        # else:
        #     total_bill = 5
        #     print(f"Your total bill is ${total_bill}.")
    elif age >= 12 and age <= 18:
    # elif age <= 18:
        print(f"Youth ticket is $7.")
        bill += 7
        # photo = input("Do you want photos? (Yes or No).")
        # if photo == "yes" or photo == "Yes":
        #     print(f"Adding $3 for photos.")
        #     total_bill = 7 + 3
        #     print(f"Your total bill is ${total_bill}.")
        # else:
        #     total_bill = 7
        #     print(f"Your total bill is ${total_bill}.")
    elif age >= 55:
        print(F"Mature ticket is FREE")
        bill += 0
    else:
        print(f"Adult ticket is $12.")
        bill += 12
        # photo = input("Do you want photos? (Yes or No).")
        # if photo == "yes" or photo == "Yes":
        #     print(f"Adding $3 for photos.")
        #     total_bill = 12 + 3
        #     print(f"Your total bill is ${total_bill}.")
        # else:
        #     total_bill = 12
        #     print(f"Your total bill is ${total_bill}.")
    
    photo = input("Do you want photos? (Yes or No).")
    if photo == "yes" or photo == "Yes":
        print(f"Adding $3 for photos.")
        bill += 3
        print(f"Your total bill is ${bill}.")
    else:
        print(f"Your total bill is ${bill}.")
else:
    print(f"Sorry, you have to grow taller before you can ride.\n")
    print(f"Minimum height is 120 cm.")