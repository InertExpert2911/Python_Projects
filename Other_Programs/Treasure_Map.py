#    1    2     3 --> COLUMN NUMBER
# ["⬜️","⬜️","⬜️"] 1 
# ["⬜️","⬜️","⬜️"] 2
# ["⬜️","⬜️","⬜️"] 3 --> ROW NUMBER
# EX: If input is 23, 2nd column 3rd row
# Placing 'X' in that position


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# Input from the user
position = input("Where do you want to put the treasure? ")

# extracting the positions from input
column_number = int(position[0]) - 1
row_number = int(position[1]) - 1

# Putting "X" into the location 
map[row_number][column_number] = "X"
# [row_number][column_number] --> To get row first, as we are displaying one below the other

# Printing all lists one after other in a different line
print(f"{row1}\n{row2}\n{row3}")