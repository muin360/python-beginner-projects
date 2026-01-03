# Day 6: Student Result Management System

def check_grade(average):
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "A-"
    elif average >= 50:
        return "B+"
    elif average >= 40:
        return "C"
    elif average >= 33:
        return "D"
    else:
        return "Fail"


student = {}


student["name"] = input("Enter Student Name: ")

subjects = ["Bangla", "English", "Math", "Science"]

total_marks = 0
passed = True


for subject in subjects:
    marks = int(input(f"Enter Marks for {subject}: "))
    student[subject] = marks
    total_marks += marks


    if marks < 33:
        passed = False



average = total_marks / len(subjects)


grade = check_grade(average)


if passed:
    result = "PASS"
else:
    result = "FAIL"



print("\n--- Student Result ---")
print(f"Name: {student['name']}")

for subject in subjects:
    print(f"{subject}: {student[subject]}")

print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print(f"Result Status: {result}")
