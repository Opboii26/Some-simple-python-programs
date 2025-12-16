# Finds whether the numbers are divisible or not

try:
    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")

if Num1 % Num2 == 0:
    print(Num1, "is divisible by", Num2)
else:
    print(Num1, "is not divisible by", Num2)