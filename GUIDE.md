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

This collection contains three Python projects:
- **File Manager**: A file manipulation utility
- **Rent Calculator**: An expense splitting application
- **Rock Paper Scissor**: An interactive game

All projects are built with Python 3.x and require no external dependencies.

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

## Installation & Setup

### Option 1: Direct Download

1. Extract the Projects folder to your desired location
2. Open Command Prompt/Terminal
3. Navigate to the Projects folder
4. Choose a project and run it

### Option 2: Clone from Repository

```bash
git clone <repository-url>
cd Projects
```

### Verification

Verify your setup:
```bash
# Check Python
python --version

# Test File Manager
cd filemanger
python "File manger.py"

# Test imports work
python -c "import os, random, datetime"
```

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

Enter your move (Rock, Paper, Scissor) or 'quit': Paper
User choice: Paper, Computer choice = Rock
Paper wins

Enter your move (Rock, Paper, Scissor) or 'quit': quit
Final Score - You: 1 | Computer: 1
```

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
