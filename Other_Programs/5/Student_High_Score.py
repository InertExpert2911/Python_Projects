# Get input from the user and use split() to split the input based on a whitespace and them in a list
student_scores = input("Input a list of student scores ").split()

# Converts each element inside the list from a string to and int data type
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

# Variable to hold highest score, initialized to 0 for now
highest_student_score = 0

# Loop goes through each score from the list and checks the condition for every iteration
for score in student_scores:
    # If score is greater than highest_student_score contents, then score value is stored inside the highest_student_score variable
    if score > highest_student_score:
        # Store the value of score, so that we replace the value every time the above if case is satisfied
        highest_student_score = score

# ----------------------------------------------------------------------------------------------------------
# You can alternatively use max(list) to get the highest item in the list
# ----------------------------------------------------------------------------------------------------------

# Print the result
print(f"The highest  student score in the class is: {highest_student_score}")
