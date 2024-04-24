# Welcoming Message
print(f"Welcome to Adding Even Numbers.")

# Create an empty list.
numbers = []
# Ask for starting number.
start = int(input(f"Input the starting number : "))
# Ask for ending of number.
ending = int(input(f"Input the ending number : "))
# Create a list of numbers from start to ending.
for n in range(int(start), int(ending) + 1):
    if n % 5 == 0 and n % 3 == 0:
        print(f"FizzBuzz")
        numbers.append("FizzBuzz")
    elif n % 5 == 0:
        print(f"Buzz")
        numbers.append("Buzz")
    elif n % 3 == 0:
        print(f"Fizz")
        numbers.append("Fizz")
    else:
        print(n)
        numbers.append(str(n))

print("Your list of numbers and FizzBuzz are : {}.".format(numbers))
