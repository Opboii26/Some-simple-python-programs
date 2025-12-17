# This program calculates passing marks from the total marks of a subject

try:
    marks = int(input("Enter the max marks of a subject: "))
except ValueError:
    print("Invalid Input!")

print("Your passing marks is: ", marks * 33/100)