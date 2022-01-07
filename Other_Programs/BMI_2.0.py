height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2;
round_off_bmi = round(bmi)

if(round_off_bmi < 18.5):
    print(f"Your BMI is {round_off_bmi}, you are underwight.")
elif(round_off_bmi > 18.5 and round_off_bmi < 25):
    print(f"Your BMI is {round_off_bmi}, you have a normal weight.")
elif(round_off_bmi > 25 and round_off_bmi < 30):
    print(f"Your BMI is {round_off_bmi}, you are slightly overweight.")
elif(round_off_bmi > 30 and round_off_bmi < 35):
    print(f"Your BMI is {round_off_bmi}, you are obese.")
else:
    print(f"Your BMI is {round_off_bmi}, you are clinically obese.")