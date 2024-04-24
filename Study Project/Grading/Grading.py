# Welcome Message
print(f"Welcome to Grading Program.")

# Module.
from Dict import student_scores

# Variable.
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Print out the result.
print(f"{student_grades}")
