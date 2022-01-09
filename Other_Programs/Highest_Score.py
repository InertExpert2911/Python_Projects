# Getting input and converting to int
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Variable to store the highest_score
highest_score = 0

# Logic to find the highest_score from the list of scores
for score in student_scores:
    if(score > highest_score):
        highest_score = score
       
# printing the higest_score
print(f"The highest score in the class is: {highest_score}")
