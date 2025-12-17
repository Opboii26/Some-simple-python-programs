import datetime

try:
    year = int(input("Enter your year: "))
    month = int(input("Enter your month: "))
    day = int(input("Enter your day: "))
except ValueError:
    print("Invalid Input! Please try again")

birth_date = datetime.date(year, month, day)
weekends = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_number = birth_date.weekday()
day_name = weekends[day_number]

print("Your day is: ", day_name)