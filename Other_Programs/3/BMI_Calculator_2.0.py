# User input
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

# calculating BMI and rounding-off the result to nearest whole number
body_mass_index = round(weight / (height ** 2))

# Using else-if conditionals to determine and print the results
if body_mass_index < 18.5:
    print(f"Your BMI is {body_mass_index}, you are underweight.")
elif body_mass_index < 25:
    print(f"Your BMI is {body_mass_index}, you have a normal weight.")
elif body_mass_index < 30:
    print(f"Your BMI is {body_mass_index}, you are slightly overweight.")
elif body_mass_index < 35:
    print(f"Your BMI is {body_mass_index}, you are obese.")
else:
    print(f"Your BMI is {body_mass_index}, you are clinically obese.")