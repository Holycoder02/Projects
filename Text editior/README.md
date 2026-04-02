# Text Editor 📝

A simple yet functional text editor built with Python's Tkinter library.

## Features

- **Create New Files**: Start fresh with a blank document
- **Open Files**: Load existing `.txt` files
- **Save Files**: Save your work with custom file names
- **Clean Interface**: User-friendly GUI with menu bar
- **Text Wrapping**: Automatic word wrapping for better readability
- **Cross-platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.6+
- Tkinter (usually comes with Python)

## Installation & Setup

1. Navigate to the Text Editor folder:
```bash
cd "Text editior"
```

2. Run the application:
```bash
python main.py
```

## Usage

1. **Create a New Document**: Click `File → New` to clear the editor
2. **Open a File**: Click `File → Open` and select a `.txt` file
3. **Save a File**: Click `File → Save` and choose a location and filename
4. **Exit**: Click `File → Exit` to close the application

## File Operations

| Operation | Steps |
|-----------|-------|
| **New** | File → New (clears current content) |
| **Open** | File → Open (browse and select a .txt file) |
| **Save** | File → Save (choose location and filename) |
| **Exit** | File → Exit (close application) |

## Keyboard Shortcuts (Using Menu)
- Use the File menu for all operations

## Code Structure

```
main.py
├── new_file()      → Clears the text editor
├── open_file()     → Opens and reads files
├── save_file()     → Saves content to file
└── GUI Setup       → Creates window and menu
```

## Example Workflow

1. Start the application
2. Type or paste text into the editor
3. Click `File → Save`
4. Choose a filename and location
5. Later, click `File → Open` to load the file again

## Notes

- Files are saved as plain text (`.txt`)
- The editor displays a success message after saving
- Works with any text-based file
- Maximum file size depends on available RAM

## Future Enhancements

- [ ] Syntax highlighting for code
- [ ] Find & Replace functionality
- [ ] Text formatting options (bold, italic)
- [ ] Font and color customization
- [ ] Auto-save feature
- [ ] Undo/Redo functionality
- [ ] Line numbering

## License

Open source - feel free to modify and use!
