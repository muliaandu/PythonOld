# Welcome Message.
print(f"Welcome to Calculator")

# Module.
import os
from Variable import ops_math, dictionary
from Function import *

# Variable.
calculator_finished = False
result = 0
number_1 = 0
number_2 = 0

# Input.

# Logic.
while not calculator_finished:
    if number_1 == 0:        
        number_1 = float(input(f"Whats the first number : "))

    for ops in ops_math:
        print(ops)

    operation_math = ""
    while operation_math not in dictionary.keys():
        operation_math = input(f"Pick an operation : ")

    if number_2 == 0:
        number_2 = float(input(f"What's the next number : "))

    continue_choosed = ""

    func = dictionary[operation_math]
    result = func(number_1 = number_1, number_2 = number_2)
    print(f"{number_1} {operation_math} {number_2} = {result}")
    # if operation_math == "+":
    #     result = addition(number_1 = number_1, number_2 = number_2)
    #     print(f"{number_1} {operation_math} {number_2} = {result}")
    # elif operation_math == "-":
    #     result = subtraction(number_1 = number_1, number_2 = number_2)
    #     print(f"{number_1} {operation_math} {number_2} = {result}")
    # elif operation_math == "*":
    #     result = multiplication(number_1 = number_1, number_2 = number_2)
    #     print(f"{number_1} {operation_math} {number_2} = {result}")
    # elif operation_math == "/":
    #     result = division(number_1 = number_1, number_2 = number_2)
    #     print(f"{number_1} {operation_math} {number_2} = {result}")
    # else:
    #     continue

    while continue_choosed == "":
        while continue_choosed != "y" and continue_choosed != "n" and continue_choosed != "end":        
            continue_choosed = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'end' to end calculator program : ").lower()
        if continue_choosed == "y":
            number_1 = result
            number_2 = 0
        elif continue_choosed == "n":
            number_1 = 0
            number_2 = 0
            os.system("cls")
        else:
            calculator_finished = True
            os.system("cls")

# Ending