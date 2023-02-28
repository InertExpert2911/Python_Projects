# Getting inputs from the user
weight = input("enter your weight in kg: ")
height = input("enter your height in m: ")

# Formula to calculate BMI = weight(kg)/height**2(m**2)

# And to perform mathematical operations, we first have to convert the type to int() if not done already
body_mass_index = int(weight)/(float(height)**2)

# Floor Division (//), to get the result as an int instead of float when you divide two numbers
# body_mass_index = int(weight)//(float(height)**2) => Decimals are cut off, no rounding

# Dropping the decimals by converting to an int()
# print(int(body_mass_index))

# Instead of chopping off the decimal places you can use round(number, the decimals you want to round-off) function to round-off to the closest integer
# (3 if the result is above 2.5)
print(round(body_mass_index))

# or you can retain upto the specified number of decimal digits
print(round(body_mass_index, 2))
