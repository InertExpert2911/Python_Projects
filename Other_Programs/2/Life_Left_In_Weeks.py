# Get user's age
age = input("What is your current age? ")

# Find the number of years left, assuming that the total lifespan is 90 years
years_left = 90 - int(age)
# print(type(years_left))

# Variables to hold info on the days, months and years
# Considering that 1 year = 365 days, 1 year = 52 weeks and 1 year = 12 months (Not considering leap years)
num_of_days_left = years_left * 365
num_of_weeks_left = years_left * 52
num_of_months_left = years_left * 12

# using f-strings to print int in a string without changing data types
print(f"You have {num_of_days_left} days, {num_of_weeks_left} weeks, and {num_of_months_left} months left.")
