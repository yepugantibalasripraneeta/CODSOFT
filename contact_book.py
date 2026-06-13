contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Address": address
        }

        print("Contact Added Successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in contacts.items():
                print(f"Name: {name}, Phone: {details['Phone']}")

    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", contacts[name]["Phone"])
            print("Address:", contacts[name]["Address"])
        else:
            print("Contact Not Found.")

    elif choice == "4":
        name = input("Enter Contact Name to Update: ")

        if name in contacts:
            contacts[name]["Phone"] = input("New Phone Number: ")
            contacts[name]["Address"] = input("New Address: ")
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found.")

    elif choice == "5":
        name = input("Enter Contact Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found.")

    elif choice == "6":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Try Again.")