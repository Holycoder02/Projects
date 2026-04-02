# Digital Clock ⏰

A simple, real-time digital clock application with a graphical user interface built using Python's Tkinter.

## Features

- **Real-Time Display**: Updates every second automatically
- **12-Hour Format**: Shows time in HH:MM:SS AM/PM format
- **Date Display**: Shows current date below the time
- **Large, Clear Font**: 50pt Calibri bold font for easy reading
- **Yellow & Black Theme**: High contrast for visibility
- **Minimal Design**: No buttons or complex controls required

## Requirements

- Python 3.6+
- Tkinter (usually comes with Python)

## Installation & Setup

1. Navigate to the Digital Clock folder:
```bash
cd "Digital Clock"
```

2. Run the clock:
```bash
python main.py
```

## Usage

1. **Start Clock**: Run `main.py` - the clock window appears automatically
2. **Display Format**:
   - **Time**: HH:MM:SS AM/PM (e.g., 02:30:45 PM)
   - **Date**: MM/DD/YY (e.g., 04/02/26)
3. **Auto Update**: Clock updates automatically every 1000ms (1 second)
4. **Close**: Click the X button to close the application

## Display Example

```
14:30:45 PM
 04/02/26
```

## Code Structure

```
main.py
├── time()        → Updates clock display every 1 second
├── strftime()    → Formats time and date
└── GUI Setup     → Creates window and label
```

## Time Format Explanation

| Format | Example | Meaning |
|--------|---------|---------|
| `%H` | 14 | Hour (00-23, 24-hour format) |
| `%M` | 30 | Minute (00-59) |
| `%S` | 45 | Second (00-59) |
| `%p` | PM | AM/PM indicator |
| `%D` | 04/02/26 | Date (MM/DD/YY) |

## Customization Options

### Change Time Format
Modify the `strftime()` format string in line 8:
```python
# Current format
string = strftime('%H:%M:%S %p \n %D')

# 24-hour format (no AM/PM)
string = strftime('%H:%M:%S \n %D')

# With day name
string = strftime('%A, %H:%M:%S %p \n %B %d, %Y')
```

### Change Appearance
Modify the label styling (line 12):
```python
# Change font - modify the tuple: (font_name, size, weight)
label = tk.Label(root, font=('Arial', 60, 'bold'), 
                 background='black', foreground='white')

# Available colors: 'red', 'blue', 'green', 'white', 'black', 'cyan', etc.
```

### Change Update Speed
Modify the refresh rate in line 10:
```python
# Update every 500ms (2x per second)
label.after(500, time)

# Update every 2000ms (every 2 seconds)
label.after(2000, time)
```

## Features Explained

| Feature | Details |
|---------|---------|
| **Real-Time Updates** | Refreshes every second using `after()` method |
| **12-Hour Format** | Automatically converts to AM/PM notation |
| **Date Display** | Shows current date in MM/DD/YY format |
| **Large Font** | 50pt size for easy visibility |
| **High Contrast** | Yellow background, black text |
| **Always On Top** | Window stays visible in foreground |

## Performance

- **CPU Usage**: Minimal (updates once per second)
- **Memory Usage**: <10MB
- **Dependencies**: Only Python standard library

## Use Cases

- Desk clock/wall display
- Learning GUI programming with Tkinter
- Time display component for other applications
- System clock verification

## Future Enhancements

- [ ] Analog clock face
- [ ] Customizable fonts and colors
- [ ] Alarm functionality
- [ ] Stopwatch/Timer
- [ ] Different time zones
- [ ] Sound notifications
- [ ] Draggable window
- [ ] Always-on-top toggle

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Clock doesn't update | Restart the application |
| Wrong time | Check your system clock |
| Distorted text | Increase window size |
| Crashing | Ensure Tkinter is installed |

## License

Open source - feel free to modify and use!
