# Ask current age.
age = int(input("What is your current age? "))
# Situation 100 years
life_years = 100
life_months = 100 * 12
life_weeks = 100 * 52
life_days = 100 * 365
# Print result.
# days_past = age * 365
# years = life_years - age
# months = life_months - (age * 12)
# weeks = life_weeks - (age * 52)
# days = life_days - (age * 365)

years = life_years - age
months = years * 12
weeks = years * 52
days = years* 365

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months
# print("You have {} days, {} weeks, and {} months left.")
result = f"You have {days} days, {weeks} weeks, {months} months, and {years} years left."
print(result)