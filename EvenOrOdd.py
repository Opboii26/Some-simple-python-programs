# This program finds whether your number is even or odd

while True:
    Number = int(input("Enter your number: "))

    try:
        if Number % 2 == 0:
            print("Your number is even\n")
        else:
            print("Your number is odd\n")
    except ValueError:
        print("Invalid input\n")