days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
month = int(input("Enter a month number between 1 to 12: "))
if 1 <= month <= 12:
    if month == 2:
        year = int(input("Kindly enter the year: "))
        if (year % 4 == 0):
            print("This month has 29 days in total")
        else:
            print("This month has 28 days in total")
    else:
        print(f"The month has {days_in_month[month]} days.")
else:
    print("Invalid number, kindly enter a month number between 1 and 12")
