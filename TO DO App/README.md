# TO DO App ✅

A simple yet powerful task management application that helps you organize and track your daily tasks with time scheduling.

## Features

- ✅ **Add Tasks** - Easily add new tasks with their scheduled times
- ✏️ **Update Tasks** - Modify task names and times
- 🗑️ **Delete Tasks** - Remove completed or unwanted tasks
- 👀 **View All Tasks** - Display all tasks with their scheduled times
- ⏰ **Time Tracking** - Associate each task with a specific time (e.g., 10:30 AM)
- 📋 **Dictionary Storage** - Efficient task-time pairing using Python dictionaries

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python libraries)

## Installation

1. Navigate to the project folder:
   ```bash
   cd "TO DO App"
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Starting the Application

When you run the application, you'll be prompted to enter the number of tasks you want to add initially:

```
---WELCOME TO THE TASK MANGEMENT APP---
Enter how many tasks you want to add = 2
Enter task 1 name = Complete project
Enter task 1 time (e.g., 10:30 AM) = 2:30 PM
Enter task 2 name = Call client
Enter task 2 time (e.g., 10:30 AM) = 3:00 PM
```

### Menu Operations

Once tasks are added, you'll see an interactive menu:

```
Enter 1-Add
2-Update
3-Delete
4-View
5-Exit:
```

#### Option 1: Add a New Task
- Enter a new task name
- Enter the task time (e.g., "10:30 AM" or "2:45 PM")
- Task is added to your list

#### Option 2: Update a Task
- Enter the name of the task you want to update
- Enter the new task name
- Enter the new time
- Task is updated successfully

#### Option 3: Delete a Task
- Enter the name of the task you want to delete
- Task is removed from your list

#### Option 4: View All Tasks
- Displays all your tasks with their scheduled times in a formatted list

#### Option 5: Exit
- Saves and closes the application

## Time Format

Tasks accept time in the following formats:
- **12-hour format**: "10:30 AM", "2:45 PM", "11:00 AM"
- **24-hour format**: "14:30", "09:15" (also supported)

Examples:
```
Complete report | Time: 2:00 PM
Lunch break | Time: 12:30 PM
Evening walk | Time: 6:00 PM
```

## Data Structure

Tasks are stored in a Python dictionary where the key is the task name and the value is the task time:

```python
tasks = {
    "Complete report": "2:00 PM",
    "Lunch break": "12:30 PM",
    "Call client": "3:30 PM"
}
```

## Example Workflow

```
1. Start application → Enter number of tasks
2. Add tasks with times
3. View all tasks to confirm
4. Update any task details as needed
5. Delete completed tasks
6. Exit when done
```

## Tips

- Task names are case-sensitive
- Each task must have a unique name
- Times can be in 12-hour or 24-hour format
- Invalid menu options will prompt you to try again
- The app validates that tasks exist before updating or deleting

## Customization

You can easily extend this app by adding:
- Task categories
- Task priorities
- Task descriptions
- Completion status tracking
- Data persistence (save to file)
- Due dates

## Troubleshooting

### Issue: "Task not found" message
- **Solution**: Ensure you're entering the exact task name (case-sensitive)

### Issue: Invalid input error
- **Solution**: Make sure you're selecting a valid menu option (1-5)

### Issue: Can't update/delete task
- **Solution**: Verify the task name exists by viewing all tasks first

## Author
Developed as a Python learning project

## License
Free to use and modify

## Version
1.0
