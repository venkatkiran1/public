phonebook = {}

def display_phonebook():
    print("\nDisplaying Phonebook:")
    for name, number in phonebook.items():
        print(f"Name: {name}, Number: {number}")

def insert_contact():
    name = input("Enter the name: ")
    number = input("Enter the number: ")
    phonebook[name] = number
    print("\nContact inserted successfully.")

def update_contact():
    name = input("Enter the name: ")
    if name in phonebook:
        number = input("Enter the updated number: ")
        phonebook[name] = number
        print("\nContact updated successfully.")
    else:
        print("\nContact not found.")

def delete_contact():
    name = input("Enter the name: ")
    if name in phonebook:
        del phonebook[name]
        print("\nContact deleted successfully.")
    else:
        print("\nContact not found.")

def delete_duplicates():
    duplicate_numbers = []
    for name1, number1 in phonebook.items():
        for name2, number2 in phonebook.items():
            if number1 == number2 and name1 != name2:
                duplicate_numbers.append(number1)
    for number in duplicate_numbers:
        for name, p_number in phonebook.items():
            if number == p_number:
                del phonebook[name]
    print("\nDuplicate contacts deleted successfully.")

def search_contact():
    name = input("Enter the name: ")
    if name in phonebook:
        print(f"\nName: {name}, Number: {phonebook[name]}")
    else:
        print("\nContact not found.")

if __name__ == '__main__':
    while True:
        print("\nTelephone Directory System:")
        print("1. Display Phonebook")
        print("2. Insert New Contact")
        print("3. Update Details on Existing Contact")
        print("4. Delete Contact")
        print("5. Delete Duplicates")
        print("6. Search Contact")
        print("7. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            display_phonebook()
        elif choice == 2:
            insert_contact()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            delete_duplicates()
        elif choice == 6:
            search_contact()
        elif choice == 7:
            print("\nExiting Telephone Directory System.")
            break
        else:
            print("\nInvalid Choice. Try Again.")
