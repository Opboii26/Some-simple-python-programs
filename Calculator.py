# Just a simple calculator

while True:
    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
    except ValueError:
        print("Invalid number! Please try again!")

    try:
        ExpectedSigns = ["+", "-", "*", "/"]
        for i in ExpectedSigns:
            availablesigns = str(i) + " "
            print(availablesigns, end="")
        sign = str(input("\nEnter your sign: "))
        if sign not in ExpectedSigns:
            raise ValueError

        if sign == "+":
            print(num1 + num2)
        elif sign == "-":
            print(num1 - num2)
        elif sign == "*":
            print(num1 * num2)
        elif sign == "/":
            print(num1 / num2)

    except ValueError:
        print("Invalid sign! Please try again!")