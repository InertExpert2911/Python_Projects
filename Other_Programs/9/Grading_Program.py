# A dictionary key:value pairs (Key: Student names, Value: exam scores)
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Empty dictionary
# This dictionary is to store student names as keys and grades as values
student_grades = {}

# Loops through every student (key) from student_scores dictionary
for student in student_scores:
    
    # Store the student score to check for grades
    get_score = student_scores[student]
    # print(get_value)
    
    # Checks for the below conditions and adds the grade based on student's score
    if get_score >= 91 and get_score <= 100:
        # Add the Key (student_name) and value (grade) to the empty list
        student_grades[student] = "Outstanding"
    elif get_score >= 81 and get_score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif get_score >= 71 and get_score <= 80:
        student_grades[student] = "Acceptable"
    else:
        # If student has a score of 70 or lower, then grade as "Fail"
        student_grades[student] = "Fail"

# Print dictionary
print(student_grades)
