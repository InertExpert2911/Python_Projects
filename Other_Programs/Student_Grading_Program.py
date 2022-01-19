# A dictionary with key: Value pairs
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# An empty dictionary.
student_grades = {}

# Grading students based on their score.
for student in student_scores:
    score = student_scores[student]

    # Checking the student score    
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
 
# Printing student grades.
print(student_grades)