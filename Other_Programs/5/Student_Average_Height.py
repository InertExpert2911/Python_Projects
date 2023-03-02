# Variable to store students height
# str.split() function is used to split a string to a list
# You can specify the separator, default separator is any whitespace
# Ex: str.split(",") -- splits based on a comma in the string
student_heights = input("Input a list of student heights ").split()

# For loops give more control than while loops
# range (start, end, step) to generate a range of numbers, here we are using range to go through from 0 to the length of the list - 1, stays in the bounds of list
# Ex: range (0, 10, 2) >>> 0 2 4 6 8 (Start (0) is included but end (10) is excluded)
for n in range(0, len(student_heights)):
    # Get the input using the index of n from the list and convert it into an integer
    student_heights[n] = int(student_heights[n])

# Variable to store the total height of students from the list, initialized to 0 for now
total_heights = 0

# Variable to store the total number of students from the list, initialized to 0 for now
total_students = 0

# Loop that goes through each item in the list and adds it to total_height variable
for height in student_heights:
    # Every time the loop runs these variables are updated
    # Height of each student in the list is added to total_height for every iteration
    total_heights += height
    # total_students is increased by 1 for every for loop iteration
    total_students += 1

# You  can alternatively use sum() and avg() functions to do the above same functionality

# Calculate average and round-off the result
average_of_student_heights = round(total_heights / total_students)

# Print result
print(average_of_student_heights)

# print(total_heights)
# print(total_students)
