# This programs calculates simple interest and compound interest

print("This program calculates simple interest and compound interest!")

def findSI(p, r, t):
    return (p*r*t)/100

def findCI(p, r, t):
    return p*(1+r)**t

while True:
    try:
        query = str(input("\nPlease choose your query: \n1. Simple interest - s\n2. Compound interest - c\nPlease choose between s/c\n\nQuery: "))
        if query != "s" and query != "c":
            raise ValueError

        # Get the values
        try:
            print("\nPlease enter the following values: ")
            p = int(input("Enter your Principal amount: "))
            r = int(input("Enter your annual rate of interest(in %): "))
            t = int(input("Enter your time(in years): "))
        except:
            print("\nSome error occured! Please try again")

        # Simple interest
        if query == "s":
            try:
                SI = findSI(p, r, t)
                print(f"\nYour simple interest is: {SI}\nAnd the Total Amount is: {p+SI}")
                break
            except:
                print("Some error occured! Please try again")

        # Compund interest
        if query == "c":
            try:
                CI = findCI(p, r, t)
                print(f"\nYour compound interest is: {CI}")
                break
            except:
                print("Some error occured! Please try again")

    except ValueError:
        print("\nInvalid Query!")