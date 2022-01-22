# TITLE CASE: "Tharun Reddy"
def format_name(f_name, l_name):
  
  # .title() function makes every starting letter of the word into uppercase (Even if there are multiple words). 
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  
  # A value is returned when we call the function. 
  # Allows us to store the result of a function into a variable.
  return f"{formatted_f_name} {formatted_l_name}"

# Storing the function result into a variable.
formatted_name = format_name("tharun", "reddy")

# Printing the stored function result.
print(formatted_name)

# print(format_name("tharun", "reddy")) this works too.
