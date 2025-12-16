# Here you can find area and perimeter of various shapes

print("Welcome to Area and Perimeter Calculator!\n")

def findPeriQuad(sides, len):
    return sides * len

while True:
    try:
        query1 = str(input("Enter what you want to find?(a/p): ")).lower()
        if query1 != "a" and query1 != "p":
            raise ValueError

        match query1:
            # Area
            case "a":
                try:
                    query2 = str(input(f"Choose from the available shapes (Square, Rectangle): ")).capitalize()
                    if query2 != "Square" and query2 != "Rectangle":
                        raise ValueError
                except ValueError:
                    print("Invalid input!")

                match query2:
                    case "Square":
                        try:
                            side = int(input("Enter your side's length: "))
                            print(f"Your area is: {side ** 2}")
                        except ValueError:
                            print("Invalid input!")

                    case "Rectangle":
                        try:
                            side1 = int(input("Enter your first side's length: "))
                            side2 = int(input("Enter your second side's length: "))

                            print(f"Your area is: {side1 * side2}")
                        except ValueError:
                            print("Invalid input!")

            # Perimeter
            case "p":
                try:
                    sides = int(input("Enter the number of sides of your quadrilateral: "))
                    if sides >= 2:
                        raise ValueError

                    len = int(input("Enter the length of each side: "))
                    print("Your perimeter is:", findPeriQuad(sides, len))
                except ValueError:
                    print("There are no quadrilaterals less then 2 sides 😂")

    except ValueError:
        print("Please enter a/p only! a = Area, p = Perimeter")