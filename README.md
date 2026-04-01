# File Manager App

A simple command-line file manager application built with Python that allows you to perform basic file operations.

## Features

- **Create Files** - Create new files in the current directory
- **View Files** - List all files in the current directory
- **Delete Files** - Remove files from the directory
- **Read Files** - Display the contents of a file
- **Edit Files** - Append new content to existing files
- **User-Friendly Menu** - Interactive menu-driven interface

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd File\ Manger
   ```

## Usage

Run the application:
```bash
python "File manger.py"
```

Once the application starts, you'll see a menu with the following options:

```
FILE MANAGER APP
1. Create a new file
2. View all files
3. Delete a file
4. Read a file
5. Edit a file
6. Exit
```

### Examples

**Create a file:**
- Select option `1`
- Enter filename: `myfile.txt`

**Read a file:**
- Select option `4`
- Enter filename: `myfile.txt`

**Edit a file:**
- Select option `5`
- Enter filename: `myfile.txt`
- Enter the content to add

**Delete a file:**
- Select option `3`
- Enter filename: `myfile.txt`

**View all files:**
- Select option `2`
- Displays all files in the current directory

**Exit:**
- Select option `6`

## Project Structure

```
File Manger/
├── File manger.py      # Main application file
├── README.md           # This file
└── sample.txt          # Sample file (optional)
```

## Functions

### `create_file(filename)`
Creates a new file with the specified filename.

### `view_all_files()`
Displays all files in the current directory.

### `delete_file(filename)`
Deletes a file from the current directory.

### `read_file(filename)`
Reads and displays the contents of a file.

### `edit_file(filename, new_content)`
Appends new content to a file.

### `main()`
Runs the main menu loop for user interaction.

## Error Handling

The application includes error handling for:
- File not found errors
- File already exists errors
- General exceptions

## Notes

- All file operations work in the current directory where the script is executed
- When editing files, new content is appended to the existing file
- The application will notify you if a file already exists or cannot be found

## License

This project is open source. Created by holycode02.

## Author

Created by **holycode02** as a simple file management utility in Python.
