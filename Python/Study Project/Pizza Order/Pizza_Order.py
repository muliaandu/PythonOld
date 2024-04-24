#  Welcome message.
print(f"Welcome to Python Pizza Deliveries! ")
print(f"""-----------------------------------------
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
      
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra Cheese for any size Pizza: +$1
-----------------------------------------""")
# Ask the size of pizza
size = input(f"What the size of Pizza do you want? (Small, Medium, Large) ")
bill = 0
if size == "Small" or size == "small":
    bill += 15
elif size == "Medium" or size == "medium":
    bill += 20
else:
    bill += 25

# Ask for pepperoni
add_pepperoni = input(f"Do you want Pepperoni? (Yes or No) ")
if add_pepperoni == "Yes" or add_pepperoni == "yes":
    if size == "Small" or size == "small":
        bill += 2
    else:
        bill += 3

# Ask for extra cheese
extra_cheese = input(f"Do you want extra cheese? (Yes or No) ")
if extra_cheese == "Yes" or extra_cheese == "yes":
    bill += 1

# Print out the result of bill
print(f"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You have been order for {size.capitalize()} Pizza
{add_pepperoni.capitalize()} to add Pepperoni
{extra_cheese.capitalize()} to extra Cheese

Your total bill is: ${bill:.2f}

Thank for your order.
Enjoy the Food.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")