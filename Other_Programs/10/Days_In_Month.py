# Leap year function


# Return keyword allows us to have an output for a function

# Eg: def add(n1, n2):
#       return n1 + n2

# We can store the result in a variable as shown below
# result = add(2, 4) >>> result = 6

# The function return's True if the year is a leap year, False if the year is not a leap year
# If the interpreter encounters a return keyword it exits out of the function by returning the value
def is_leap(year):
    
    if year % 4 == 0:
        
        if year % 100 == 0:
            
            if year % 400 == 0:
                # Return True if the year is leap year
                return True
            else:
                # Return False if the year is not a leap year
                return False
        else:
            return True
    else:
        return False

# Function takes Year and Month as inputs and returns the number of days in the given year of a given month
def days_in_month(year, month):
    
    # Catch Exception
    # If the month is above 12 or below 1
    if month > 12 or month < 1:
        # Return this string as output of this function
        return "Invalid month inputted"
    
    # List that holds number of days in each month of a year
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # If  the year is leap year and the user is checking for the 2nd month then return the value
    if is_leap(year) and month == 2:
        
        # Return 29 as leap year's will have 29 days in the month of February
        return 29
    
    # Return the items from the list by deducting the month by 1 as list indexing starts from 0
    return month_days[month - 1]
    
    # -------------------------------------------- ANOTHER METHOD ---------------------------------------------------
    
    # ## If the inputted year is not a leap year then return the days in the month from the month_days variable
    # else:
    #     ## Return the items from the list by deducting the month by 1 as list indexing starts from 0
    #     return month_days[month - 1]
    
    # -------------------------------------------- ANOTHER METHOD ---------------------------------------------------
    


# Get the inputs
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# Store the value returned from the function days_in_month() to days variable
days = days_in_month(year, month)

# Print output
print(days)
