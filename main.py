# Student Grade Manager

student_name = input("Enter student name: ")

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))

average = (grade1 + grade2 + grade3) / 3

print("\n----- Student Report -----")
print("Student:", student_name)
print("Average:", round(average, 2))

if average >= 10:
    print("Result: Passed")
else:
    print("Result: Failed")
