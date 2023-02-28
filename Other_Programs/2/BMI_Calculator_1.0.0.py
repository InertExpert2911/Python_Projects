# Getting inputs from the user
weight = input("enter your weight in kg: ")
height = input("enter your height in m: ")

# Formula to calculate BMI = weight(kg)/height**2(m**2)

# And to perform mathematical operations, we first have to convert the type to int() if not done already
body_mass_index = int(weight)/(float(height)**2)

# Dropping the decimals by converting to an int()
print(int(body_mass_index))
