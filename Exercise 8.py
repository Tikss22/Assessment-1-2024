name_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search_names = input("Enter a name: ")
if search_names in name_list:
    print(f"{search_names} is in the name list")
else:
    print(f"{search_names} name not found in the list")
