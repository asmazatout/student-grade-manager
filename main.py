# Student Grade Manager

student_name = input("Enter student name: ")

grades = []

number_of_grades = int(input("How many grades do you want to enter? "))

for i in range(number_of_grades):

    while True:
        grade = float(input(f"Enter grade {i + 1}: "))

        if 0 <= grade <= 20:
            grades.append(grade)
            break
        else:
            print("Invalid grade! Enter a value between 0 and 20.")

average = sum(grades) / len(grades)

print("\n----- Student Report -----")
print("Student:", student_name)
print("Grades:", grades)
print("Average:", round(average, 2))

if average >= 10:
    print("Result: Passed")
else:
    print("Result: Failed")
