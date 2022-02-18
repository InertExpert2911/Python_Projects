# Importing PrettyTable class from prettytable package imported
from prettytable import PrettyTable, DOUBLE_BORDER

# Creating an object.
table = PrettyTable()

# Changing the style of the table.
table.set_style(DOUBLE_BORDER)

# Printing the object
# We see an empty table at this point and not the location where the object is stored.
# print(table)

# add_column() is a method of the PrettyTable class.
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# See which type of align is set.
print(table.align)

# Modifying the attribute to set the alignment to left.
table.align = "l"

#  Checking after changing the alignment to "l".
print(table.align)

print(table)
