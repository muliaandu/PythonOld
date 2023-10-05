# Ask for height.
height = input("Enter your height in m: ")
# Ask for weight.
weight = input("Enter your weight in kg: ")
# Print the BMI result.
result_in_float = float(weight) / (float(height) ** 2)
result_in_int = int(result_in_float)
print("Your BMI Point is {}.".format(result_in_int))
print("Your BMI Point with Decimal result is {:.2f}.".format(result_in_float))
bmi = result_in_float

# Create logic to showing the result of BMI
if bmi <= 18.5:
    print("Your BMI is {:.2f}, You are underweight.".format(bmi))
elif bmi <= 25:
    print("Your BMI is {:.2f}, You are normal Weight.".format(bmi))
elif bmi <= 30:
    print("Your BMI is {:.2f}, You are overWeight.".format(bmi))
else:
    print("Your BMI is {:.2f}, You are obese.".format(bmi))