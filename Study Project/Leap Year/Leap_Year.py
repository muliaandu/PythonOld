# Welcoming message.
print(f"Checking the Leap Year !")
# Asking what year want to check.
year = int(input(f"Which year do you want to check? "))
# Create a logic here and show the result.
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print(f"Leap Year.")
        else:
            print(f"Not Leap Year.")    
    else:
        print(f"Leap Year.")
else:
    print(f"Not Leap Year.")