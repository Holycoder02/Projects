# Projects Guide

A comprehensive guide to understanding, running, and extending the Projects collection.

## Table of Contents

1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [Project Details](#project-details)
4. [Installation & Setup](#installation--setup)
5. [Usage Instructions](#usage-instructions)
6. [Troubleshooting](#troubleshooting)
7. [Development & Extension](#development--extension)
8. [Best Practices](#best-practices)

---

## Overview

This collection contains thirteen Python projects:
- **File Manager**: A file manipulation utility
- **Rent Calculator**: An expense splitting application
- **Rock Paper Scissor**: An interactive game
- **Tic Tac Toe**: A two-player GUI game
- **Text Editor**: A simple file editor
- **Digital Clock**: A real-time clock display
- **TO DO App**: A task management system with time tracking
- **Image Slideshow**: An image viewer with automatic cycling
- **Payment QR Code Generator**: UPI payment QR code generator
- **Contact Book**: A contact management system
- **Spell Checker**: A spelling error detection and correction tool
- **Student Grade Management System**: A student grade tracking application
- **WhatsApp Automation Messages**: Automated WhatsApp message scheduling

All projects are built with Python 3.x. GUI projects (Tic Tac Toe, Text Editor, Digital Clock, Image Slideshow, Student Grade Management System) require Tkinter and some require PIL. The Payment QR Code Generator requires qrcode and pillow libraries. The Spell Checker requires pyspellchecker library. The WhatsApp Automation requires twilio library.

---

## Getting Started

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.6 or higher
- **RAM**: Minimal (< 100MB)
- **Storage**: < 10MB for all projects

### Checking Python Installation

```bash
python --version
# or on some systems
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/)

---

## Project Details

### 1. File Manager 📂

**Purpose**: Manage files in your current working directory

**Key Features**:
- Create new files
- List all files
- Read file contents
- Edit files (append mode)
- Delete files

**Use Cases**:
- Learning file I/O operations
- Basic file management tasks
- Understanding exception handling

**Code Structure**:
```
create_file()      → Creates files
view_all_files()   → Lists directory contents
read_file()        → Displays file contents
edit_file()        → Appends to files
delete_file()      → Removes files
```

**Typical Workflow**:
1. Start the program → Import the module
2. Call functions as needed
3. Handle success/error messages
4. Review results

---

### 2. Rent Calculator 💰

**Purpose**: Calculate and distribute shared expenses fairly among residents

**Key Features**:
- Multi-person support
- Tracks individual names
- Multiple expense categories
- Input validation
- Currency formatting (Indian Rupees)
- Save results to files

**Use Cases**:
- Splitting hostel/apartment expenses
- Calculating shared utility costs
- Creating expense records
- Fair distribution calculations

**Expense Categories**:
1. **Rent**: Base accommodation cost
2. **Food**: Combined food expenses
3. **Electricity**: Usage-based calculation (units × rate)
4. **Water**: Monthly water bill
5. **Internet**: Internet/connectivity bill

**Calculation Logic**:
```
Total Expenses = Rent + Food + (Electricity Units × Rate) + Water + Internet
Per Person Share = Total Expenses ÷ Number of Persons
```

**Output**:
- Individual breakdowns
- Total amounts owed
- Timestamped file saves

---

### 3. Rock Paper Scissor Game 🎮

**Purpose**: Play the classic game against the computer

**Key Features**:
- Interactive round-by-round gameplay
- Score tracking (player vs computer)
- Random computer opponent
- Multiple rounds support
- Clean exit with final scores

**Game Rules** (Standard):
- Rock beats Scissor
- Scissor beats Paper
- Paper beats Rock
- Same choices = Tie

**Game Flow**:
```
Player Input → Computer Choice → Compare → Determine Winner
                                              ↓
                                         Update Scores
                                              ↓
                                         Continue or Quit
```

**Valid Inputs**:
- "Rock", "rock", "ROCK" (all variations)
- "Paper", "paper", "PAPER"
- "Scissor", "scissor", "SCISSOR"
- "Quit" or "quit" (exits game)

---

### 4. Tic Tac Toe Game 🎮

**Purpose**: Play two-player Tic Tac Toe with graphical interface

**Key Features**:
- Visual 3×3 game board with Tkinter
- Two-player gameplay (Player X vs Player O)
- Automatic win detection (8 combinations)
- Draw/Tie detection
- Winning squares highlighted in green
- Reset button for multiple games
- Turn indicator label

**Game Rules**:
- Players alternate turns (X always goes first)
- Click empty squares to place your mark
- First to get 3 in a row wins
- Rows: top, middle, bottom
- Columns: left, center, right
- Diagonals: top-left to bottom-right, top-right to bottom-left

**Winning Combinations** (8 total):
```
Horizontal: [0,1,2] [3,4,5] [6,7,8]
Vertical:   [0,3,6] [1,4,7] [2,5,8]
Diagonal:   [0,4,8] [2,4,6]
```

**Board Layout**:
```
 0 | 1 | 2
-----------
 3 | 4 | 5
-----------
 6 | 7 | 8
```

---

### 5. Text Editor 📝

**Purpose**: Simple file editor for creating and editing text files

**Key Features**:
- Create new documents
- Open existing `.txt` files
- Save files with custom names
- Menu-based interface (File menu)
- Text wrapping for readability
- Cross-platform compatibility

**Menu Options**:
| Option | Action |
|--------|--------|
| File → New | Clear editor (start fresh) |
| File → Open | Load a `.txt` file |
| File → Save | Save current content to file |
| File → Exit | Close application |

**Supported File Types**:
- `.txt` (Text files)
- Any plain text format

**Workflow**:
```
Start → Type/Paste → Save → Later Open → Edit → Save Again
```

---

### 6. Digital Clock ⏰

**Purpose**: Display current time and date in real-time

**Key Features**:
- Live 1-second updates
- 12-hour format with AM/PM
- Current date display (MM/DD/YY)
- Large 50pt font for visibility
- Yellow background, black text
- Minimal, clutter-free design

**Time Format**:
```
HH:MM:SS AM/PM
MM/DD/YY
```

**Example Display**:
```
02:30:45 PM
 04/02/26
```

**Customization Options**:
- Change font (modify `font=('calibri', 50, 'bold')`)
- Change colors (modify `background`, `foreground`)
- Change update speed (modify `after(1000)` milliseconds)
- Modify time format (adjust `strftime()` format string)

---

### 7. TO DO App ✅

**Purpose**: Manage daily tasks with time scheduling

**Key Features**:
- Dictionary-based task storage
- Task with time tracking (e.g., "10:30 AM")
- Add new tasks anytime
- Update task names and times
- Delete completed tasks
- View all tasks with times
- User-friendly menu interface

**Menu Operations**:
| Option | Action |
|--------|--------|
| 1 | Add new task with time |
| 2 | Update existing task name and time |
| 3 | Delete task by name |
| 4 | View all tasks with times |
| 5 | Exit application |

**Data Structure**:
```python
tasks = {
    "Task Name": "HH:MM AM/PM",
    "Complete project": "2:30 PM",
    "Lunch break": "1:00 PM"
}
```

**Time Format**:
- 12-hour format: "10:30 AM" or "2:45 PM"
- 24-hour format: "14:30" (also supported)

**Workflow**:
```
Start → Add tasks with times → View all → Update/Delete → Exit
```

---

### 8. Image Slideshow 🖼️

**Purpose**: Display rotating images in a GUI window

**Key Features**:
- Load multiple images from file paths
- Auto-resize to 1080×1080 pixels
- Automatic cycling (3-second delays)
- Button control to start slideshow
- Uses PIL for image manipulation
- Tkinter-based GUI window
- Non-blocking image updates using `root.after()`

**Supported Image Formats**:
- JPG / JPEG
- PNG
- AVIF
- GIF (static images)
- WebP
- BMP

**Image Cycling**:
- Images rotate every 3 seconds (3000 ms)
- Continuous loop using modulo arithmetic
- Non-blocking updates with `root.after()`

**Configuration**:
```python
image_size = (1080, 1080)  # Change resize dimension
root.after(3000, update_image)  # Change delay in milliseconds
```

**Setup Instructions**:
1. Add image paths to `image_paths` list in code
2. Ensure all images exist on your system
3. Run the program
4. Click "Start Slideshow" button to begin
5. Images automatically rotate every 3 seconds

---

### 9. Payment QR Code Generator 💳

**Purpose**: Generate QR codes for UPI payment methods

**Key Features**:
- Support for 3 payment apps (PhonePe, Paytm, Google Pay)
- UPI URL schema implementation
- QR code display on screen
- Optional saving to image files
- Customizable recipient name and merchant code
- Automatic QR code generation

**UPI URL Format**:
```
upi://pay?pa={UPI_ID}&pn={Recipient_Name}&mc={Merchant_Code}
```

**Setup Requirements**:
```bash
pip install qrcode[pil]
pip install pillow
```

**Supported Payment Apps**:
1. **PhonePe**: UPI standard protocol
2. **Paytm**: UPI standard protocol
3. **Google Pay**: UPI standard protocol

**Workflow**:
```
Input UPI ID → Generate URLs → Create QR Codes → Display → Optional: Save to disk
```

**Customization**:
```python
# Modify recipient name
"Your Business Name"  # Change this

# Modify merchant code
"1234"  # Merchant code

# Save to file (uncomment lines)
# phonepe_qr.save("phonepe_qr.png")
# paytm_qr.save("paytm_qr.png")
# googlepay_qr.save("googlepay_qr.png")
```

**Output**:
- Three QR codes displayed in separate windows
- One for each payment app
- Users can scan directly with phone

---

### 10. Contact Book 📇

**Purpose**: Manage personal contacts with name, age, email, and phone number

**Key Features**:
- Add new contacts with details (name, age, email, mobile)
- View individual contact information
- Update existing contact details
- Delete contacts from the system
- Search contacts by name (case-insensitive)
- Count total contacts in the book
- Duplicate contact prevention
- Interactive menu-driven interface

**Menu Operations**:
| Option | Action |
|--------|--------|
| 1 | Add new contact |
| 2 | View specific contact |
| 3 | Update contact details |
| 4 | Delete contact |
| 5 | Search contacts by name |
| 6 | Count total contacts |
| 7 | Exit application |

**Data Structure**:
```python
contacts = {
    "John Doe": {
        "age": 28,
        "email": "john@example.com",
        "mobile": "9876543210"
    }
}
```

**Workflow**:
```
Start → Add/View/Update/Delete/Search → View all → Exit
```

**Search Functionality**:
- Case-insensitive partial matching
- Finds contacts by name pattern
- Displays full contact details when found

---

### 11. Spell Checker 🔤

**Purpose**: Check and correct spelling errors in text using PySpellChecker

**Key Features**:
- Real-time spell checking
- Automatic word correction suggestions
- Interactive text input interface
- Misspelled words highlighted with corrections
- Case-insensitive checking
- Continuous checking without restarting
- Dictionary-based validation

**Setup Requirements**:
```bash
pip install pyspellchecker
```

**How It Works**:
1. User enters text to check
2. Each word is validated against dictionary
3. Misspelled words are identified
4. Suggested corrections are displayed
5. Corrected text is shown to user

**Output Format**:
```
Correcting "speling" to "spelling"
Corrected Text: spelling is important
```

**Supported Languages**:
- English (primary support)
- Extensible for other languages

**Workflow**:
```
Enter Text → Check Words → Suggest Corrections → Display Results → Continue or Exit
```

**Limitations**:
- May not recognize proper names (people, places)
- Limited by built-in dictionary
- Context-based corrections not supported
- Slang and informal language not recognized

---

### 12. Student Grade Management System 📊

**Purpose**: Manage student grades with CLI and GUI interfaces

**Key Features**:
- Add students with grades
- Update student grades
- Delete student records
- View all students and grades
- Duplicate student prevention
- Input validation (grades 0-100 for GUI)
- Success and error notifications
- Two interface options: CLI and GUI

**Two Implementations**:

**A. CLI Version (main.py)**:
- Command-line text interface
- Menu-driven interaction
- Simple and quick to run
- No dependencies beyond Python

**B. GUI Version (main2.py)**:
- Tkinter graphical interface
- Colored buttons for easy navigation
- Dialog boxes for input
- Formatted student list display
- Professional appearance
- Better user experience

**Menu Operations**:
| Option | Action |
|--------|--------|
| 1 | Add new student |
| 2 | Update student grade |
| 3 | Delete student |
| 4 | View all students |
| 5 | Exit application |

**Data Structure**:
```python
student_grade = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78
}
```

**GUI Features**:
- Color-coded buttons (green for Add, blue for Update, red for Delete, orange for View)
- Text area displaying formatted student list
- Dialog-based input for names and grades
- Real-time student list updates
- Success/error message boxes

**Workflow**:
```
Start → Add/Update/Delete/View → Display Results → Continue or Exit
```

**Grade Validation**:
- GUI version: Enforces 0-100 range
- Prevents duplicate students
- Numeric input validation

## Installation & Setup

### Option 1: Direct Download
### Running Tic Tac Toe

```bash
cd "Tic Tac Toe"
python main.py
```

**Gameplay**:
1. Window opens showing 3×3 grid
2. X goes first
3. Click empty squares to place marks
4. Game ends when someone gets 3 in a row or board is full
5. Click "Reset Game" button to play again

### Running Text Editor

```bash
cd "Text editior"
python main.py
```

**Workflow**:
1. Editor window opens with blank page
2. Type or paste text
3. File → Open to load file
4. File → Save to save as new file
5. File → New to clear and start fresh

### Running Digital Clock

```bash
cd "Digital Clock"
python main.py
```

**Features**:
1. Clock window displays immediately
2. Time updates every second
3. Shows current time and date
4. Close with window X button

### Running TO DO App

```bash
cd "TO DO App"
python main.py
```

**Usage Example**:
```
---WELCOME TO THE TASK MANGEMENT APP---
Enter how many tasks you want to add = 2
Enter task 1 name = Complete report
Enter task 1 time (e.g., 10:30 AM) = 2:00 PM
Enter task 2 name = Call client
Enter task 2 time (e.g., 10:30 AM) = 3:30 PM

Today's tasks are:
  - Complete report | Time: 2:00 PM
  - Call client | Time: 3:30 PM

Enter 1-Add
2-Update
3-Delete
4-View
5-Exit: 1
Enter task you want to add = Lunch meeting
Enter task time (e.g., 10:30 AM) = 12:30 PM
Task 'Lunch meeting' at 12:30 PM has been added successfully
```

### Running Image Slideshow

```bash
cd "Image slide show"
python main.py
```

**Requirements**:
```bash
pip install pillow
```

**Setup**:
1. Edit `main.py` and add your image file paths to the `image_paths` list
2. Use raw strings with `r` prefix for Windows paths
3. Ensure all image files exist
4. Run the program
5. Click "Start Slideshow" to begin
6. Images rotate every 3 seconds automatically

**Example Image Paths**:
```python
image_paths = [
    r"C:\Users\YourName\Pictures\vacation.jpg",
    r"C:\Users\YourName\Pictures\family.png",
    r"C:\Users\YourName\Downloads\photo.avif",
]
```

### Running Payment QR Code Generator

```bash
cd "Accept payment with paython"
python main.py
```

**Requirements**:
```bash
pip install qrcode[pil]
pip install pillow
```

**Usage Example**:
```
Enter your upi id: merchant@hdfcbank
# Three QR code windows appear for:
# 1. PhonePe
# 2. Paytm
# 3. Google Pay
# Users can scan any code with their payment app
```

**Save QR Codes**:
Uncomment these lines in `main.py` to save as image files:
```python
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
googlepay_qr.save("googlepay_qr.png")
```

### Running WhatsApp Automation Messages

```bash
cd "Whatsapp automations messages"
python main.py
```

**Requirements**:
```bash
pip install twilio
```

**Twilio Setup**:
1. Create account at https://www.twilio.com
2. Get Account SID and Auth Token from Console
3. Update credentials in `main.py`
4. Enable WhatsApp messaging in your account

**Usage Example**:
```
Enter the recipient name = Raju
Enter the recipient Whatsapp number with country code (e.g, +12345) = +916299538998
enter the message you want to send to Raju: Hello! This is an automated message
enter the date to send the message (YYYY-MM-DD): 2026-04-10
enter the time to send the message (HH:MM in 24hour format): 14:30
Message scheduled to be sent to Raju at 2026-04-10 14:30:00.
Message sent successfully! Message SID: SM1234567890abcdef
```

**Important Notes**:
- Keep script running until message is sent
- Phone numbers must include country code (e.g., +916299538998)
- Time must be in 24-hour format (00:00 to 23:59)
- Schedule for future date and time only
- Never commit Twilio credentials to version control

### Running Contact Book

```bash
cd "Contact book"
python main.py
```

**Example Usage**:
```
Contact Book app
1. Add contact
2. View contacts
3. Update contact
4. Delete contact
5. Search contact
6. Count contacts
7. Exit

Enter you choice = 1
Enter contact name = John Doe
enter age = 28
Enter email = john@example.com
Enter mobile number = 9876543210
Contact John Doe added successfully!
```

### Running Spell Checker

```bash
cd "Spell checker"
python main.py
```

**Requirements**:
```bash
pip install pyspellchecker
```

**Example Usage**:
```
---Spell Checkker---
Enter text to check (or type "exit" to quit): hallo world
Correcting "hallo" to "hello"
Corrected Text : hello world
Enter text to check (or type "exit" to quit): exit
Closing the program
```

### Running Student Grade Management System

**CLI Version**:
```bash
cd "Student Grade mangement system"
python main.py
```

**GUI Version**:
```bash
cd "Student Grade mangement system"
python main2.py
```

**Workflow**:
```
1. Select option from menu
2. Enter student details (name and grade)
3. View list of all students
4. Update or delete as needed
5. Exit when done
```

**GUI Features**:
- Professional window interface with colored buttons
- Dialog boxes for input
- Real-time student list with formatted display
- Color-coded operations (Add: Green, Update: Blue, Delete: Red, View: Orange)

---

## Usage Instructions

### Running File Manager

```bash
cd filemanger
python "File manger.py"
```

**Example Usage**:
```python
from File_manger import create_file, view_all_files, read_file

# Create a file
create_file("myfile.txt")

# View all files
view_all_files()

# Read file content
read_file("myfile.txt")
```

### Running Rent Calculator

```bash
cd "Rent Calculator"
python app.py
```

**Workflow**:
1. Enter number of people (must be positive)
2. Enter names for each person
3. Enter all expense amounts
4. Review calculated shares
5. Results are automatically saved

**Sample Input**:
```
Number of persons: 3
Names: Alice, Bob, Charlie
Rent: 30000
Food: 9000
Electricity units: 100
Rate per unit: 5
Water: 1500
Internet: 999
```

### Running Rock Paper Scissor

```bash
cd "Rock Paper Scissor"
python main.py
```

**Game Session Example**:
```
Enter your move (Rock, Paper, Scissor) or 'quit': Rock
User choice: Rock, Computer choice = Paper
Paper wins
Tic Tac Toe game won't start
**Solution**:
- Ensure Tkinter is installed: `python -m tkinter`
- Check for syntax errors in main.py
- Verify button positions in grid layout

#### Issue: Text Editor won't open files
**Solution**:
- Check file permissions
- Ensure file format is `.txt`
- Try opening from the dialog (don't type path)

#### Issue: Digital Clock shows wrong time
**Solution**:
- Check system clock settings
- Verify timezone is correct
- Restart the application

---

## Troubleshooting

### Common Issues & Solutions

#### Issue: "Python is not recognized"
**Solution**: 
- Reinstall Python and check "Add Python to PATH"
- Use `python3` instead of `python`
- Check your PATH environment variables

#### Issue: "Module not found" in File Manager
**Solution**:
- Ensure you're in the correct directory
- Check the filename spelling (case-sensitive on some systems)
- Verify the file extension is `.py`

#### Issue: Rent Calculator won't accept input
**Solution**:
- Enter only positive numbers (no negative values)
- Don't include currency symbols or commas
- Ensure input is numeric

#### Issue: Game doesn't accept my move
**Solution**:
- Check spelling: Rock, Paper, Scissor (capital first letter)
- Avoid extra spaces
- Use only these three options

#### Issue: File operations fail
**Solution**:
- Check directory permissions
- Ensure disk has free space
- Verify file names are valid
- Check for special characters in filenames

---

## Development & Extension

### Extending File Manager

**Add Features**:
```python
# Move files
def move_file(source, destination):
    # Implementation
    pass

# Copy files
def copy_file(source, destination):
    # Implementation
    pass

# Search for files
def search_files(pattern):
    # Implementation
    pass
```

### Extending Rent Calculator

**Possible Enhancements**:
- Add expense categories
- Calculate who owes whom
- Support for different currencies
- Monthly history tracking
- Payment settlement algorithm

### Extending Rock Paper Scissor

**Game Improvements**:
- Add Lizard & Spock rules
- Difficulty levels
- Play best of N rounds
- Time-limited rounds
- Player vs Player mode

---

## Best Practices

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Include docstrings for functions

### Error Handling
- Always validate user input
- Handle exceptions gracefully
- Provide helpful error messages
- Log important operations

### File Management
- Use proper file paths
- Handle file encoding explicitly (UTF-8 recommended)
- Close files after operations
- Backup important data

### Testing
- Test with edge cases
- Verify error messages
- Test with different inputs
- Check file permissions

### Documentation
- Keep README.md updated
- Add usage examples
- Document all functions
- Provide clear instructions

---

## Quick Reference

### File Manager Functions
| Function | Parameters | Returns |
|----------|-----------|---------|
| create_file() | filename (str) | None |
| view_all_files() | None | None |
| read_file() | filename (str) | None |
| edit_file() | filename (str), content (str) | None |
| delete_file() | filename (str) | None |

### Rent Calculator Inputs
- Number of persons (integer, > 0)
- Person names (any string)
- Rent amount (integer, ≥ 0)
- Food amount (integer, ≥ 0)
- Electricity (units, integer)
- Rate per unit (integer)
- Water bill (integer, ≥ 0)
- Internet bill (integer, ≥ 0)

### Rock Paper Scissor Moves
- "Rock" or "rock"
- "Paper" or "paper"
- "Scissor" or "scissor"
- "Quit" or "quit" (to exit)

---

## Additional Resources

### Python Documentation
- [Official Python Docs](https://docs.python.org/3/)
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Random Module](https://docs.python.org/3/library/random.html)
- [DateTime Module](https://docs.python.org/3/library/datetime.html)

### Learning Resources
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Real Python Tutorials](https://realpython.com/)
- [W3Schools Python](https://www.w3schools.com/python/)

---

## Support & Feedback

If you encounter issues:
1. Check this guide's troubleshooting section
2. Review the relevant project's README.md
3. Check Python version compatibility
4. Review error messages carefully

---

**Document Version**: 1.0  
**Last Updated**: April 2, 2026  
**Python Version**: 3.6+
