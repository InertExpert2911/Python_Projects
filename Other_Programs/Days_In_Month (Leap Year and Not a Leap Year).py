# Leap year function.
# Returning True if the year satisfies the conditions of a Leap year, else False.
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# Function to return the number of days in a month, if it is a Leap year it is 29 days in Feb , else returning the number of the days in Jan-Dec.
def days_in_month(year, month):
  """DocString -- To Document our Functions."""
  
  # Checking the month value of the user to avoid OutOfBounds Error.  
  if month > 12 and month < 1:
      return "Invalid Month"
  
  # Number of days for all months in a year.
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
 
  # Checking if it is a leap year and month is Feb
  if is_leap(year) and month == 2:
    return 29
  else:
    return month_days[month - 1]

# Taking input from the user
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# Calling days_in_month and storing the output in a variable.
days = days_in_month(year, month)

# Printing the result.
print(days)
