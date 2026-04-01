# File Manager

A simple command-line file management utility built with Python.

## Features

- **Create Files**: Create new files in the current directory
- **View Files**: Display all files in the current directory
- **Delete Files**: Remove files from the current directory
- **Read Files**: View the contents of specific files
- **Edit Files**: Append content to existing files

## Functions

| Function | Description |
|----------|-------------|
| `create_file(filename)` | Creates a new file with the specified name |
| `view_all_files()` | Lists all files in the current directory |
| `delete_file(filename)` | Deletes the specified file |
| `read_file(filename)` | Reads and displays the content of a file |
| `edit_file(filename, new_content)` | Appends content to a file |

## Usage

Import the module and use the functions:

```python
from File_manger import create_file, view_all_files, delete_file, read_file, edit_file

# Create a new file
create_file("example.txt")

# View all files
view_all_files()

# Read a file
read_file("example.txt")

# Edit a file
edit_file("example.txt", "New content here")

# Delete a file
delete_file("example.txt")
```

## Error Handling

The utility includes error handling for:
- FileExistsError: When trying to create a file that already exists
- FileNotFoundError: When trying to read or delete a non-existent file
- General exceptions: Catches unexpected errors

## Requirements

- Python 3.x
- No external dependencies

## Notes

- All operations are performed on the current working directory
- File names are case-sensitive on Linux/Mac systems
