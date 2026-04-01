
# Python Projects Repository 🚀

Welcome to a collection of practical Python projects! This repository contains multiple standalone applications, each designed to solve real-world problems. Whether you're learning Python fundamentals or building useful utilities, you'll find well-documented, beginner-to-intermediate level projects here.

**Repository Goal:** Build practical Python skills by creating real tools you can actually use.

---

## 📚 Table of Contents

1. [Projects](#-projects-in-this-repository)
2. [Installation](#-installation--setup)
3. [Project Details](#-detailed-project-guides)
4. [Usage Examples](#-usage-examples)
5. [Troubleshooting](#-troubleshooting--faq)
6. [Learning Path](#-learning-path)
7. [Contributing](#-contributing)

---

## 📚 Projects in This Repository

### 1. 📁 File Manager
**Level:** Beginner | **Python Skills:** File I/O, Functions, Control Flow

A full-featured command-line utility for managing files. Perfect for learning file operations in Python.

**What It Does:**
- Create new files with custom names
- Browse all files in your directory
- Read and display file contents
- Append text to existing files
- Delete files safely
- User-friendly interactive menu

**Best For:**
- Learning file I/O operations
- Quick file management from terminal
- Understanding function organization
- Python beginners (Beginner Level)

**Quick Run:**
```bash
python "File manger.py"
```

---

### 2. 🏠 Rent Calculator
**Level:** Beginner-Intermediate | **Python Skills:** Arithmetic, Data Validation, Loops, File Operations

An intelligent expense splitter designed for shared living situations. Handles multiple expenses and calculates fair distribution among roommates.

**What It Does:**
- Track multiple expenses (rent, food, utilities, internet, water)
- Calculate electricity costs based on units consumed
- Distribute costs fairly among residents
- Handle remainder amounts intelligently
- Generate individual bills with resident names
- Save calculation results to timestamped files
- Validate all user input

**Best For:**
- Roommates splitting rent and utilities
- Student groups sharing apartments
- Hostels managing shared expenses
- Learning input validation and arithmetic
- Understanding file export functionality

**Quick Run:**
```bash
python "Rent Calculator/app.py"
```

---

## �️ Installation & Setup

### Step 1: Check Python Installation

**Windows (Command Prompt or PowerShell):**
```cmd
python --version
```

**Mac/Linux (Terminal):**
```bash
python3 --version
```

You should see Python 3.x (version 3.6 or higher). If not, [download Python here](https://www.python.org/downloads/).

### Step 2: Download Repository

Clone or download this repository to your computer.

### Step 3: Navigate to Project

**Windows:**
```cmd
cd "File Manger"
```

**Mac/Linux:**
```bash
cd "File Manger"
```

### Verify Installation

Check that Python is working:
```bash
python --version
# Output should show Python 3.x.x
```

---

## 📖 Detailed Project Guides

### File Manager - Complete Guide

#### How It Works

The File Manager presents you with a numbered menu. You select an option, the program asks for details, and it performs the action.

#### Menu Options Explained

| Option | What It Does | Example Input |
|--------|------------|---------|
| **1 - Create** | Creates a new empty file | `notes.txt` |
| **2 - View** | Lists all files in current folder | (no input needed) |
| **3 - Delete** | Removes a file permanently | `old_file.txt` |
| **4 - Read** | Shows entire file contents | `notes.txt` |
| **5 - Edit** | Adds text to end of file | `notes.txt` + new text |
| **6 - Exit** | Closes the program | (no input needed) |

#### Step-by-Step Walkthrough

**Creating Your First File:**
1. Run `python "File manger.py"`
2. You'll see the menu - press `1` for Create
3. Type a filename: `myfile.txt`
4. Press Enter - file is created!

**Editing a File:**
1. From menu, press `5` for Edit
2. Type filename: `myfile.txt`
3. Type content: `This is my first note`
4. Press Enter - content added to file

**Reading Your File:**
1. From menu, press `4` for Read
2. Type filename: `myfile.txt`
3. Full file contents will display

#### Important Notes

- **Edit vs Replace:** Option 5 ADDS text to the end of files, it doesn't replace them
- **Filenames:** Always include extensions (`.txt`, `.csv`, `.md`, etc.)
- **Current Directory:** Files are created/deleted in the folder where you ran the program
- **Case Sensitive:** On Mac/Linux, `file.txt` and `File.txt` are different. Windows ignores case.

---

### Rent Calculator - Complete Guide

#### How It Works

The Rent Calculator guides you through entering all shared expenses, then calculates how much each person owes. It handles uneven divisions fairly.

#### Detailed Walkthrough

**Step 1: Number of Residents**
```
Enter the number of persons sharing = 3
```
Tell it how many people are splitting costs.

**Step 2: Enter Names**
```
Enter name of person 1 = Raj
Enter name of person 2 = Priya
Enter name of person 3 = Arjun
```
This enables individual billing.

**Step 3: Enter Each Expense**
```
Enter hostel/flat rent = 15000
Enter amount spent on food = 3000
Enter total electricity spend (in units) = 150
Enter charge per unit = 5
Enter water bill = 500
Enter internet bill = 1500
```

**Step 4: View Results**

The program displays:
- Complete expense breakdown
- Total bill amount
- Per-person share
- How remainder is distributed
- Individual bills for each person

**Step 5: Save Results (Optional)**
```
Do you want to save results to file? (yes/no) = yes
Results saved to: rent_calc_20260401_143025.txt
```
Creates a timestamped file with all calculations.

#### Example - Real Calculation

**Input:**
- 3 people: Rahul, Neha, Vikram
- Rent: ₹12,000
- Food: ₹2,000
- Electricity: 100 units × ₹4 = ₹400
- Water: ₹600
- Internet: ₹1,200

**Calculation:**
- Total: ₹16,200
- Per person: ₹16,200 ÷ 3 = ₹5,400 each
- Remainder: ₹0

**Output:**
```
BILL BREAKDOWN
Rent:             ₹12000.00
Food:             ₹2000.00
Electricity:      ₹400.00
Water:            ₹600.00
Internet:         ₹1200.00
TOTAL BILL:       ₹16200.00

PER PERSON (3 persons):
Rahul:  ₹5400.00
Neha:   ₹5400.00
Vikram: ₹5400.00
```

#### Smart Remainder Handling

What if the total doesn't divide evenly?

**Example:** ₹16,201 ÷ 3 = ₹5,400 each + ₹1 remainder

**The calculator does this:**
- First person pays ₹5,401 (gets the extra ₹1)
- Other two pay ₹5,400 each

Very fair!

---

## 📂 Repository Structure

```
File Manger/
│
├── 📄 File manger.py          # File Manager application
├── 📄 README.md               # This comprehensive guide
├── 📄 sample2.txt             # Sample file for testing
│
├── 📁 Rent Calculator/        # Rent calculator project
│   ├── 📄 app.py             # Main calculator application
│   └── 📄 sample.txt         # Sample calculation file
│
└── 📁 .git/                   # Version control system
```

---

## 📝 Usage Examples

### File Manager Examples

**Example 1: Create and Read a Shopping List**
```
1. Press 1 to create
2. Type "shopping.txt"
3. Press 1 again
4. Type "milk.txt"
5. Press 4 to read
6. Type "shopping.txt"
7. See contents displayed
```

**Example 2: Manage Multiple Files**
```
Press 2 to view all files
→ shopping.txt
→ notes.txt
→ data.csv

Press 5 to edit shopping.txt
Add: "Buy eggs"
```

---

### Rent Calculator Examples

**Example 1: Simple Two-Person Split**
```
Persons: 2 (Anne, Bob)
Rent: ₹10,000
Food: ₹2,000
Electricity (50 units × ₹10): ₹500
Water: ₹500
Internet: ₹1,000

Total: ₹14,000
Each pays: ₹7,000
Result: Anne ₹7,000, Bob ₹7,000
```

**Example 2: Four-Person Complex Split**
```
Persons: 4 (Arjun, Bhavna, Chirag, Diana)
Rent: ₹20,000
Food: ₹4,000
Electricity: ₹800
Water: ₹800
Internet: ₹2,000

Total: ₹27,600
Base amount: ₹6,900 each
Remainder: ₹0
Result: Each person pays ₹6,900
```

---

## 🔧 Troubleshooting & FAQ

### "Python: command not found"
**Problem:** Python isn't accessible from terminal

**Solution:**
- **Windows:** Use `python3` instead of `python`
- **Mac/Linux:** Ensure Python3 is installed: `brew install python3`
- **All:** Add Python to PATH (Google "Add Python to PATH [your OS]")

### "File not found" Error

**When Reading/Deleting Files:**
1. Use option 2 to view all available files
2. Make sure the filename matches exactly (case-sensitive on Mac/Linux)
3. Ensure file is in the current directory

### "File already exists" in File Manager

**Problem:** Trying to create a file that already exists

**Solution:**
- Use a different filename
- Or delete the existing file first (option 3)

### "Invalid input" in Rent Calculator

**Problem:** Entered text when numbers expected, or negative numbers

**Solution:**
- Enter only positive whole numbers
- Don't include currency symbols
- Don't include commas in numbers

### "Cannot save file" in Rent Calculator

**Problem:** Permission denied when saving results

**Solution:**
- Check folder permissions
- Ensure you have write access to the directory
- Move to a different directory and try again

### FAQ

**Q: Can I use these programs together?**
A: Yes! Use File Manager to create expense files, then Rent Calculator to split costs.

**Q: Can I modify these programs?**
A: Absolutely! You're encouraged to customize and learn from the code.

**Q: Do I need internet to run these?**
A: No, both programs work completely offline.

**Q: Can I use these for real expenses?**
A: Yes! They're designed for practical use with real roommates.

**Q: How do I add more projects?**
A: Create a new folder, add your Python script, and update this README.

---

## 🎓 Learning Path

### Beginner - Start Here
1. **First:** File Manager
   - Learn: File operations, functions, user input, control flow
   - Time: 1-2 hours to understand
   - Practice: Create and edit test files

2. **Second:** Rent Calculator
   - Learn: Input validation, arithmetic, loops, file export
   - Time: 2-3 hours to understand
   - Practice: Calculate your own expenses

### Intermediate - Challenge Yourself
- Modify File Manager to:
  - Search for files
  - Show file size
  - Show creation date
- Modify Rent Calculator to:
  - Add utility costs breakdown
  - Export to CSV format
  - Track monthly history

### Advanced - Build Your Own
- Create a new project in this repository
- Combine features from both projects
- Add a web interface
- Create a GUI version

---

## 💡 Pro Tips & Best Practices

### File Manager Tips
- ✓ Always include file extensions when creating files
- ✓ Use descriptive filenames (not "file1", use "todo_list")
- ✓ Check option 2 before deleting to confirm file exists
- ✓ Make backups before deleting important files
- ✓ Use .txt for text, .csv for data, .md for notes

### Rent Calculator Tips
- ✓ Calculate immediately after expenses are finalized
- ✓ Save results for your records
- ✓ Use actual names for clear accountability
- ✓ Round expenses to nearest rupee
- ✓ Review calculations before sharing with roommates
- ✓ Keep saved files organized by month

---

## 🔮 Future Projects Roadmap

This repository will grow over time! Planned projects:

| Project | Description | Difficulty |
|---------|-------------|-----------|
| **Password Manager** | Secure password storage | Intermediate |
| **Todo List App** | Task management system | Beginner |
| **Budget Tracker** | Monthly budget monitoring | Intermediate |
| **Expense Report** | Generate expense reports | Intermediate |
| **Note Taking App** | Rich note management | Beginner |
| **Calculator GUI** | Graphical calculator | Intermediate |

---

## 🤝 Contributing & Support

### Found a Bug?
- Try the [Troubleshooting](#-troubleshooting--faq) section
- Check Python version is 3.x or higher
- Verify you're in correct directory

### Have Suggestions?
- Want a new feature?
- Have a bug fix?
- Ideas for new projects?

Feel free to contribute!

---

## 🎉 Getting Help

If you're stuck:

1. **Check the examples** in the guide above
2. **Read error messages carefully** - they often explain the problem
3. **Verify Python installation** - run `python --version`
4. **Check the FAQ** section for common issues
5. **Review the code comments** for implementation details

---

## 📄 License

This projects repository is **open source**. You're free to:
- ✓ Use these projects
- ✓ Modify them for your needs
- ✓ Share them with others
- ✓ Learn from the code
- ✓ Build upon them

---

## 👨‍💻 Author & Community

Created by **holycode02**  
Passionate about building practical Python solutions for everyday problems.

---

## ✨ Support This Project

If these projects help you learn Python:
- ⭐ Give this repository a star
- 🔄 Share with others learning Python
- 💬 Provide feedback
- 🚀 Check back for new projects!

---

**Last Updated:** April 2026  
**Happy Coding! 💻🎉**
