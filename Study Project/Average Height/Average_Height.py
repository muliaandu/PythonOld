# Welcome message.
print(f"Welcome to Average Height Calculator.")

# Create a blank of list.
student_height = []
# Input a number of students.
number_of_student = int(input(f"How much student should be check? "))
student = 0
# Create a logic to adding Student Height to a list
for numb in range (number_of_student):
    heights = int(input(f"Please input Student Height number {student + 1} : "))
    student_height.append(heights)
    student += 1
else :
    pass
# Create a logic to count the number then averaging the number.
sum_height = sum(student_height)
len_height = len(student_height)
average_height = sum_height / len_height
# Print out the result.
print(f"List of Students Height : {student_height}")
print(f"Total of Student Height : {sum_height}")
print(f"How many Student are there : {len_height}")
print(f"The Average Height from all Height : {average_height:.2f}")