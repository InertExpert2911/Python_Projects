# Getting input and converting to int
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Varibales to store sum and total and count
sum_of_heights = 0
total_height = 0
count_of_students = 0 # This is to find the number of elements in a list

# Logic for calculating average student height
for student in student_heights:
    sum_of_heights += student
    count_of_students += 1
    total_height = sum_of_heights/count_of_students
 
# Rounding the total_height
print(round(total_height))