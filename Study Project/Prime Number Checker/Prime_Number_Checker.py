# Welcoming message.
print(f"Welcome to Prime Number Checker.")

# Variable.

# Input.
number = int(input(f"Check this number: "))

# Logic.
def prime_checker(number):
    is_prime = True
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"It's a prime number.")
    else:
        print(f"It's not a prime number.")

# Print out the result.
prime_checker(number)