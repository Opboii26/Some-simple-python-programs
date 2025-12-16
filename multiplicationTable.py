# Writes multiplication table of any number

while True:
    try:
        Num = int(input("\nEnter your number: "))
        for i in range(1, 11):
            print(f"{Num} X {i} = {Num * i}")
    except ValueError:
        print("Invalid input! Please try again!")