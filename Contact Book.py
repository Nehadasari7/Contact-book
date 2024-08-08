def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact for {name} added successfully.")

def view_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.")

def search_contact(contacts, search_term):
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        address = input("Enter the new address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact for {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Deleted contact: {name}")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(contacts, search_term)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
