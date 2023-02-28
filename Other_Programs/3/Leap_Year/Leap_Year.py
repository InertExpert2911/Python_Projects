# Input
year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    
    if year % 100 == 0:
        
        if year % 400 == 0:
            
            print("Leap year.")
            
        else:
            print("Not leap year.")
    else:
        print("Leap year.")    
else:
    print("Not leap year.")

# REFER TO THE ATTACHED PDF FOR MORE INFO
# For a year to be leap it has to follow the below conditions:

# CONDITION - 1a: If the year is cleanly divisible by 4 leaving no remainder, then you gotta check condition-2
# CONDITION - 1b: If the year is not cleanly divisible by 4, then it is NOT a leap year

# CONDITION - 2a: If the year is cleanly divisible by 100 leaving no remainder, then you gotta check condition-3
# CONDITION - 2b: If the year is not cleanly divisible by 100, then it is a leap year

# CONDITION - 3a: If the year is cleanly divisible by 4, 100 and 400 then the year is a leap year
# CONDITION - 3b: If the year is cleanly divisible by 4 and 100 but not cleanly divisible by 400 then it is not a leap year
