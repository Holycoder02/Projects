import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: Created successfully.")

    except FileExistsError:
        print(f"File Name {filename}: Already exists! ")

    except Exception as e:
        print(f'An error occurred!')

def view_all_files():
    files = os.listdir()
    if not files:
        print('No file found!')
    else:
        print('Files in directory:')
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')
    
    except FileNotFoundError:
        print('File not found!')

    except Exception as e:
        print(f'An error occured!')

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}' :\n{content}")

    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print('An error occurred!')

def edit_file(filename, new_content):
    try:
        with open(filename, 'a') as f:
            f.write(new_content + "\n")
            print(f"Content added to {filename} Successfully!")

    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print('An error occurred!')

def main():
    while True:
        print('FILE MANAGER APP')
        print('1. Create a new file')
        print('2. View all files')
        print('3. Delete a file')
        print('4. Read a file')
        print('5. Edit a file')
        print('6. Exit')

        choice = input('Enter your choice (1-6) = ')

        if choice == '1':
            filename = input("Enter the file-name to create: ")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("enter the file-name to delete: ")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter the file-name to read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter the file-name to edit: ")
            new_content = input("Enter the content to add: ")
            edit_file(filename, new_content)

        elif choice == '6':
            print('Exiting the application. Goodbye!')
            break

        else:
            print('Invalid choice!')

if __name__ == "__main__":
    main()

