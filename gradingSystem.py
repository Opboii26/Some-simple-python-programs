# Tell the grades of the student according to its marks
try:
    noSubject = int(input("Enter the number of subjects: "))
    marks_per_subject = int(input("Enter max marks per subject: "))

    if noSubject <= 0 or marks_per_subject <= 0:
        raise ValueError("Numbers must be positive")
except ValueError:
    print("Invalid input! Please enter positive integers only.")
    exit()

totalMarks = noSubject * marks_per_subject
marks = 0

for i in range(1, noSubject + 1):
    marks += int(input(f"Enter your marks in subject {i}: "))

percentage = (marks / totalMarks) * 100
print(f"Your percentage is: {percentage}%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 85:
    grade = "A"
elif percentage >= 80:
    grade = "A-"
elif percentage >= 75:
    grade = "B+"
elif percentage >= 70:
    grade = "B"
elif percentage >= 65:
    grade = "C+"
elif percentage >= 60:
    grade = "C"
elif percentage >= 55:
    grade = "D+"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("Your grade is:", grade)
