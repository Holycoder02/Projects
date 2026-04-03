# Contact Book Application

A simple Python command-line application for managing your personal contacts with essential features like adding, viewing, updating, deleting, and searching contacts.

## Overview

This Contact Book application helps you organize and manage your personal contacts efficiently. Store contact information including name, age, email, and mobile number in a structured format.

---

## Features

- **Add Contact** - Add new contacts with name, age, email, and mobile number
- **View Contacts** - Display details of a specific contact
- **Update Contact** - Modify existing contact information
- **Delete Contact** - Remove contacts from the book
- **Search Contact** - Find contacts by name (partial search supported)
- **Count Contacts** - Get total number of contacts in your book
- **Exit** - Close the application

---

## Requirements

- Python 3.x
- No external packages required (uses only built-in Python libraries)

---

## Installation

1. Ensure Python 3.x is installed on your system
2. Download or clone this repository
3. Navigate to the Contact Book directory

---

## How to Run

```bash
python main.py
```

The application will start with an interactive menu.

---

## Usage Guide

### 1. **Add Contact**
```
Enter your choice = 1
Enter contact name = John Doe
enter age = 28
Enter email = john@example.com
Enter mobile number = 9876543210
Contact John Doe added successfully!
```

### 2. **View Contact**
```
Enter your choice = 2
Enter contact name to view = John Doe
Name: John Doe, Age: 28, Mobile Number: 9876543210 Email: john@example.com
```

### 3. **Update Contact**
```
Enter your choice = 3
Enter name to update = John Doe
Enter updated contact = 29
Enter updated email = newemail@example.com
Enter updated mobile number = 9999999999
Contact updated!
```

### 4. **Delete Contact**
```
Enter your choice = 4
Enter name to delete = John Doe
Contact John Doe deleted successfully!
```

### 5. **Search Contact**
```
Enter your choice = 5
enter name to search = John
Found - Name: John Doe, Age: 28, Mobile Number: 9876543210, Email: john@example.com
```

### 6. **Count Contacts**
```
Enter your choice = 6
Total contacts in your book: 5
```

### 7. **Exit**
```
Enter your choice = 7
Goodbye! closing the program
```

---

## Data Storage

**Note:** This application stores contacts in memory only during runtime. When the program exits, all data is lost. To persist data between sessions, consider implementing file-based storage (JSON/CSV) or a database.

---

## Project Structure

```
Contact Book/
│
└── main.py          # Main application file
```

---

## Features Explanation

### Dictionary-Based Storage
Contacts are stored in a Python dictionary with the following structure:
```python
{
    'John Doe': {
        'age': 28,
        'email': 'john@example.com',
        'mobile': '9876543210'
    }
}
```

### Duplicate Prevention
The system prevents adding duplicate contacts by checking if a name already exists.

### Search Functionality
The search feature uses case-insensitive partial matching, so searching "john" will find "John Doe".

---

## Learning Concepts

This project demonstrates:
- Dictionary data structures
- While loops and user input handling
- Conditional statements (if/elif/else)
- String manipulation and formatting
- Loop iteration with `.items()`
- Function-like operations without using functions

---

## Potential Improvements

- Add data persistence (save/load from file)
- Input validation for email and phone numbers
- Age validation (ensure it's a valid number)
- Function-based code structure for better modularity
- GUI version using Tkinter
- Database integration for larger datasets
- Export contacts to CSV/PDF
- Contact categories/groups
- Favorite contacts feature

---

## Known Limitations

- Data not persistent (lost on program exit)
- Search shows variable names instead of actual values
- No input validation for email format
- No phone number format validation
- Limited to command-line interface

---

## Author

Created as an educational project to demonstrate Python fundamentals.

---

## License

This project is free to use and modify for educational purposes.

---

## Support

For issues or questions:
1. Ensure Python 3.x is installed
2. Check that you're in the correct directory
3. Verify the file has proper permissions
4. Check the menu options (1-7) are valid choices

---

**Happy organizing your contacts!**
