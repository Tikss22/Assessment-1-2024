# Ask the user to input the password
password = input("Please enter the password: ")
# Define the correct password
correct_password = "12345"
# Start a loop that will continue until the user enters the correct password
while password != correct_password:
    # Print a message if the entered password is incorrect
    print("Incorrect password. Please try again.")
    # Ask the user to input the password again if it was incorrect
    password = input("Please enter the password: ")
# Once the correct password is entered, print "Correct"
print("Correct")