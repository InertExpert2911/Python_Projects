# Import math module
import math


# Function to calculate number of paint cans needed with parameters
# Eg: def function(parameter_1, parameter_2):
def paint_calculator(height, width, cover):
    
    # Number of cans = (wall height x wall width) ÷ coverage per can
    total_area = height * width
    
    # math.ceil(x) -- function math ceiling returns the smallest integer higher or equal to x
    number_of_cans_needed = math.ceil(total_area / cover)
    
    # Print the result and round-off the value to its nearest whole number
    print(f"You'll need {number_of_cans_needed} cans of paint.")

# Inputs
test_height = int(input("Height of wall: "))
test_width = int(input("Width of wall: "))

# Eg: The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall
coverage = 5

# Call the above defined function and pass the keyword arguments
# Eg: function(argument_1, argument_2) -- Positional arguments
# Keyword Arguments: function(parameter_1 = argument_1, parameter_2 = argument_2) -- Keyword arguments
paint_calculator(height=test_height, width=test_width, cover=coverage)
