# Welcomeing Message.
print(f"Welcome to Paint Area Calculator.")

# Variable
height = int(input(f"Height of wall : "))
width = int(input(f"Width of wall : "))
coverage = int(input(f"Coverage per can : "))
number_of_can = 0

# Calculator
def number_can(height, width, coverage):
    number_of_can = round((height * width) / coverage)
    print(f"You should buy {number_of_can} cans of paint.")

# Print out the result
number_can(height, width, coverage)