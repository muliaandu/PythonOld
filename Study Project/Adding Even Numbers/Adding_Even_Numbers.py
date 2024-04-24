# Welcoming Message
print(f"Welcome to Adding Even Numbers.")

# Create an empty list.
numbers = []
even_number = 0
list_of_even_number = []
# Ask for starting number.
start = int(input(f"Input the starting number : "))
# Ask for ending of number.
ending = int(input(f"Input the ending number : "))
# Create a list of numbers from start to ending.
for n in range(int(start), int(ending) + 1):
    numbers.append(str(n))
    if int(n) % 2 == 0:
        even_number += int(n)
        list_of_even_number.append(str(n))
    else:
        pass 

print("Your list of numbers are : {}.".format(numbers))
print("Your list of even numbers are : {}.".format(list_of_even_number))
print("Your total from even_number is {}.".format(even_number))
