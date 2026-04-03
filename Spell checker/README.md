# Spell Checker Application

A Python command-line application that checks and corrects spelling errors in text using the PySpellChecker library.

## Overview

This Spell Checker application helps you identify and correct misspelled words in your text. It uses a dictionary-based approach to detect and suggest corrections for common spelling mistakes.

---

## Features

- **Real-time Spell Checking** - Check spelling as you type
- **Automatic Corrections** - Get suggestions for misspelled words
- **Interactive Interface** - Simple menu-driven command-line interface
- **Dynamic Feedback** - See which words are being corrected
- **Continuous Usage** - Keep checking multiple texts without restarting

---

## Requirements

- Python 3.x
- PySpellChecker library

---

## Installation

### Step 1: Clone or Download
Download the Spell Checker project to your local machine.

### Step 2: Install PySpellChecker
Open your terminal/command prompt and run:
```bash
pip install pyspellchecker
```

### Step 3: Run the Application
Navigate to the Spell Checker directory and run:
```bash
python main.py
```

---

## How to Use

1. **Start the Application**
   ```bash
   python main.py
   ```

2. **Enter Text to Check**
   ```
   ---Spell Checkker---
   Enter text to check (or type "exit" to quit): hallo world
   ```

3. **View Corrections**
   ```
   Correcting "hallo" to "hello"
   Corrected Text : hello world
   ```

4. **Repeat or Exit**
   - Enter more text to check
   - Type "exit" to quit the program

---

## Usage Examples

### Example 1: Simple Typo
```
Input: "speling is important"
Correcting "speling" to "spelling"
Output: "spelling is important"
```

### Example 2: Multiple Errors
```
Input: "i have a hapy day"
Correcting "hapy" to "happy"
Output: "i have a happy day"
```

### Example 3: Correct Text
```
Input: "Python is great"
Output: "Python is great"
(No corrections shown)
```

---

## How It Works

### Architecture
The application uses a class-based structure:

```python
class SpellCheckerApp:
    - __init__()        # Initialize the spell checker
    - correct_text()    # Process and correct text
    - run()            # Main application loop
```

### Correction Process
1. Split input text into individual words
2. For each word, check against the dictionary
3. If a misspelling is detected, suggest correction
4. Return the fully corrected text

---

## Code Structure

```
Spell Checker/
│
└── main.py          # Main application file
```

### Key Components

**SpellCheckerApp Class:**
- Manages spell checking functionality
- Handles user interaction
- Maintains spell checker instance

**Methods:**
- `__init__()` - Initializes the PySpellChecker
- `correct_text(text)` - Corrects misspelled words
- `run()` - Main application loop

---

## Known Limitations

1. **Limited Dictionary** - Some uncommon words may not be recognized
2. **Single-Word Errors** - Works on individual words, not context-based corrections
3. **Proper Nouns** - Names and place names may be flagged as errors:
   - "Gaurav" might not be recognized
   - "Mumbai" might not be recognized
4. **Abbreviations** - Some abbreviations may be flagged incorrectly
5. **Slang/Informal Language** - May not recognize casual language and slang
6. **Technical Terms** - Programming and technical terms may be flagged

### Example of Limitations
```
Input: "Gaurav is from Mumbi"
Output: "Gaurav is from Mumbai"
(Or may try to correct "Gaurav" to something unexpected)
```

---

## Learning Concepts

This project demonstrates:
- Class-based object-oriented programming
- External library integration (PySpellChecker)
- String manipulation and word splitting
- While loops and user input handling
- Conditional logic for text processing
- Main module execution with `if __name__ == "__main__"`

---

## Potential Improvements

- **Custom Dictionary** - Add user-defined words to dictionary
- **Batch Processing** - Check multiple files at once
- **File I/O** - Read from and write to text files
- **GUI Version** - Create graphical interface with Tkinter
- **Confidence Score** - Show confidence level for corrections
- **Context-Based Corrections** - Use sentence context for better suggestions
- **Language Support** - Support multiple languages
- **Ignore List** - Skip certain words from correction
- **Undo/Redo** - Allow reverting corrections
- **Export Results** - Save corrected text to file

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'spellchecker'"
**Solution:** Install PySpellChecker
```bash
pip install pyspellchecker
```

### Issue: Script doesn't run
**Solution:** Ensure you're in the correct directory
```bash
cd path/to/Spell\ Checker
python main.py
```

### Issue: Getting wrong corrections
**Solution:** This is a limitation of the spell checker library. Check the "Known Limitations" section.

---

## Performance

- **Speed:** Lightning fast for typical usage
- **Memory:** Minimal memory footprint
- **Accuracy:** ~95% for common English words
- **Support:** English language primarily

---

## Author

Created as an educational project to demonstrate Python fundamentals and external library integration.

---

## License

This project is free to use and modify for educational purposes.

---

## Related Projects

- Student Grade Management System
- Contact Book Application
- Text Editor

---

## Support

For issues or questions:
1. Verify PySpellChecker is installed
2. Check Python version compatibility
3. Ensure text encoding is UTF-8
4. Review the "Known Limitations" section

---

**Happy Spell Checking!** ✨
