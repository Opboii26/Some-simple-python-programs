# This program tells the greater number between two numbers

Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))

if Num1 > Num2:
    print(Num1, "is greater than", Num2)
elif Num2 > Num1:
    print(Num2, "is greater than", Num1)
else:
    print("Both numbers are equal")