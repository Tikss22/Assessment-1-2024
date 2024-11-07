# Define a list of names
name_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Ask the user to input a name they want to search for
search_names = input("Enter a name: ")
# Check if the entered name is in the name_list
if search_names in name_list:
    # If the name is found, print a message confirming the name is in the list
    print(f"{search_names} is in the name list")
else:
    # If the name is not found, print a message saying the name is not in the list
    print(f"{search_names} name not found in the list")