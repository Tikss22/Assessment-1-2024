password = input("Please enter the password: ")
correct_password = "12345"
while password != correct_password:
    print("Incorrect password. Please try again.")
    password = input("Please enter the password: ")
print("Correct")
