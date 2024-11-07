# Dictionary to store the number of days in each month
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# Step 1: Ask the user to input a month number
month = int(input("Enter a month number between 1 to 12: "))
# Step 2: Check if the entered month number is valid (between 1 and 12)
if 1 <= month <= 12:
    # Step 3: If the month is February (month == 2), handle leap year check
    if month == 2:
    # Ask the user for the year to check for leap year
        year = int(input("Kindly enter the year: "))
   # Step 4: Check if the year is a leap year (divisible by 4)
        if (year % 4 == 0):
            print("This month has 29 days in total")
        else:
  # If not a leap year, February has 28 days
            print("This month has 28 days in total")
    else:
 # Step 5: For all other months, print the number of days using the dictionary
        print(f"The month has {days_in_month[month]} days.")
else:
# Step 6: If the entered month is not valid, display an error message
    print("Invalid number, kindly enter a month number between 1 and 12")