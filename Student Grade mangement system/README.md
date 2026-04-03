# Student Grade Management System

A comprehensive Python application for managing student grades with two different interfaces: command-line and graphical user interface (GUI).

## Overview

This project provides a simple yet effective way to manage student grades. It allows you to add, update, delete, and view student records. Two implementations are provided to suit different preferences.

---

## Files

### 1. **main.py** - Command-Line Interface (CLI)
A simple command-line based application that uses text input/output for user interaction.

**Features:**
- Add new students with their grades
- Update existing student grades
- Delete student records
- View all students in the system
- Interactive menu-driven interface
- Input validation

**How to Run:**
```bash
python main.py
```

**Usage:**
```
Student Grade Management System
1. Add Student
2. Update Student Grade
3. Delete Student
4. View All Students
5. Exit

Enter your choice = 1
Enter student name = John
Enter student grade = 85
Added John with a 85
```

**Best For:**
- Quick testing and learning
- Server environments without GUI support
- Users comfortable with command-line interfaces

---

### 2. **main2.py** - Graphical User Interface (GUI)
A modern Tkinter-based GUI application with an interactive window interface.

**Features:**
- Professional window-based interface
- Colored action buttons (Add, Update, Delete, View)
- Dialog boxes for user input
- Real-time student list display with formatted output
- Input validation (grades must be 0-100)
- Duplicate student prevention
- Success and error message boxes
- User-friendly design

**How to Run:**
```bash
python main2.py
```

**Benefits:**
- Intuitive point-and-click interface
- No command-line knowledge required
- Better user experience
- Professional appearance

**Best For:**
- End-users and students
- Educational purposes
- Demonstration and presentations
- Users who prefer graphical interfaces

---

## Requirements

- Python 3.x
- No external packages required (both use built-in Python libraries)
  - `main.py` uses only standard library
  - `main2.py` uses Tkinter (included with Python)

---

## Installation

1. Make sure Python 3.x is installed on your system
2. Download or clone this repository
3. Navigate to the project directory

---

## Functionality

Both implementations offer the same core functionality:

### **Add Student**
- Enter student name
- Enter grade (0-100 for GUI version)
- Student is added to the system
- Duplicate check prevents adding the same student twice

### **Update Student Grade**
- Enter the name of the student to update
- Enter the new grade
- System updates the grade if student exists
- Error message if student not found

### **Delete Student**
- Enter the name of the student to delete
- Confirms deletion with success message
- Error message if student not found

### **View All Students**
- Display all students currently in the system
- Shows student names and their grades
- Displays "No students found" if system is empty

---

## Comparison

| Feature | main.py (CLI) | main2.py (GUI) |
|---------|---------------|----------------|
| Interface Type | Command-line | Graphical Window |
| External Dependencies | None | None (Tkinter built-in) |
| Input Method | Text input prompts | Dialog boxes |
| Output Display | Console text | GUI text area |
| Grade Validation | Basic | 0-100 range check |
| User-friendly | Moderate | High |
| Learning Purpose | Great | Excellent |

---

## Example Usage

### Using main.py (CLI):
```
$ python main.py
Student Grade Management System
1. Add Student
2. Update Student Grade
3. Delete Student
4. View All Students
5. Exit
Enter your choice = 1
Enter student name = Alice
Enter student grade = 92
Added Alice with a 92
```

### Using main2.py (GUI):
1. Click "Add Student" button
2. Enter name in dialog box
3. Enter grade in next dialog box
4. See confirmation message
5. Click "View All Students" to see updated list

---

## Data Storage

**Note:** Both applications store student data in memory only. When the program exits, all data is lost. To persist data between sessions, you would need to implement file saving (JSON/CSV) or database storage.

---

## Future Enhancements

- Save/load student data from files
- Database integration for persistent storage
- Grade statistics (average, highest, lowest)
- Search and filter options
- Export grades to CSV or PDF
- Password protection
- Multi-user support

---

## Author

Created as an educational project to demonstrate Python fundamentals including:
- Dictionary data structures
- Function definitions
- Conditional logic
- GUI programming with Tkinter
- User input handling
- Error handling

---

## License

This project is free to use and modify for educational purposes.

---

## Support

If you encounter any issues:
1. Ensure Python 3.x is installed
2. Check that you're in the correct directory
3. Verify file permissions
4. For GUI issues, ensure Tkinter is installed (`python -m tkinter` to test)

---

**Happy Learning!** Choose the interface that works best for your needs.
