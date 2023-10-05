# Welcome message.
print(f"Welcome to the Love Calculator!")
# Ask for the first name.
name_men = input(f"What is Men's name? ").lower()
# Ask for the second name.
name_women = input(f"What is Women's name? ").lower()
# Count the True Love letters in the name.
count_true_men = name_men.count("t") + name_men.count("r") + name_men.count("u") + name_men.count("e")
count_true_women = name_women.count("t") + name_women.count("r") + name_women.count("u") + name_women.count("e")
count_love_men = name_men.count("l") + name_men.count("o") + name_men.count("v") + name_men.count("e")
count_love_women = name_women.count("l") + name_women.count("o") + name_women.count("v") + name_women.count("e")
count_true = count_true_men + count_true_women
count_love = count_love_men + count_love_women
result = count_true + count_love

# combined_name = name_men + name_women
# t = combined_name.count("t")
# r = combined_name.count("r")
# u = combined_name.count("u")
# e = combined_name.count("e")

# l = combined_name.count("l")
# o = combined_name.count("o")
# v = combined_name.count("v")
# e = combined_name.count("e")

# true = t + r + u + e
# love = l + o + v + e

# result = str(true) + str(love)

# Print out the result.
# For Love scores less than 10 or greater than 90, the message should be:
if int(result) < 10 or int(result) > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
# # For Love scores between 40 and 50, the message should be:
elif int(result) >= 40 and int(result) <= 50:
    print(f"Your score is {result}, you are alright together.")
# # Otherwise, the message will just be their score.
else:
    print(f"Your score is {result}.")