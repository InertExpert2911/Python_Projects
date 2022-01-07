
height = (input("enter your height in m: "))
weight = input("enter your weight in kg: ")

height_sqaured = float(height) ** 2

BMI = int(weight)/(height_sqaured)
print(round(BMI))