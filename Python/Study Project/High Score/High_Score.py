# Welcome Message.
print(f"Welcome to High Score Calculator.")

# Ask for the Student Scores.
student_scores = input(f"Input a list of student score : ").split()
high_score = 0
# Create a logic to pick a maximize score.
for n in range(len(student_scores)) :
    student_scores[n] = int(student_scores[n])
    if high_score < student_scores[n]:
        high_score = student_scores[n]
    else:
        pass

print(f" You are input this Student Score : {student_scores}")
print(f"The highest score in the class is : {high_score}")