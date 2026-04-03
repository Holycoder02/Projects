contacts = { }

while True:
    print('\nContact Book app')
    print("1. Add contact")
    print("2. View contacts")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contacts")
    print("7. Exit")

    choice = input('Enter you choice = ')

    if choice == '1':
        name = input('Enter contact name = ')
        if name in contacts:
            print(f'Contact {name} already exists!')

        else:
            age = input('enter age = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f'Contact {name} added successfully!')

    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {age}, Mobile Number: {mobile} Email: {email}')


        else:
            print('Contact not found!')

    elif choice == '3':
        name = input('Enter name to update = ')
        if name in contacts:
            age = input('Enter updated contact =')
            email =  input('Enter updated email = ')
            mobile = input('Enter updated mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}

        else:
            print('Contact not found!')

    elif choice == '4':
        name = input('Enter name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact {name} deleted successfully!')

        else:
            print('Contact not found!')

    elif choice == '5':
        name = input('enter name to search = ')
        found = False
        for name, contact in contacts.items():
            if name.lower() in name.lower():
                print(f'Found - Name {name}, Age:{contact["age"]}, Mobile Number:{contact["mobile"]}, Email:{contact["email"]}')
                found = True

        if not found:
            print('Contact not found!')

    elif choice == '6':
        print(f'Total contacts in your book: {len(contacts)}')

    elif choice == '7':
        print('Goodbye! closing the program')
        break

    else:
        print('Invalid choice! please try again!')



