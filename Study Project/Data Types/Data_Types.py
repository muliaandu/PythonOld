# 1. Ask for two digit number.
two_digit_number = str(input('Type a two digit number (10 - 99) : '))
# 2. Print result from first digit plus second digit.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print("{} + {} = {}".format(first_digit, second_digit, int(first_digit) + int(second_digit)))