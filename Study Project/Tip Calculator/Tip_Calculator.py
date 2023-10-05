# #1. Print a welcome message.
print("Welcome to the tip calculator")
# #2. Ask how much the bill
total_bill = float(input("What was the total bill? $"))
# #3. Ask how many people to split the bill
split_bill = int(input("How many people to split the bill? "))
# #4. Ask how many percentage of tip
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#5. Print the result of how much each person should pay
result = (total_bill / split_bill) + ((total_bill / split_bill) * (percentage_tip / 100))
print("Each person should pay: ${}".format(round(result, 2)))
print("Each person should pay: ${:.2f}".format(result))