# Tic Tac Toe Game 🎮

A classic two-player Tic Tac Toe game with a graphical user interface built using Python's Tkinter.

## Features

- **Two Player Gameplay**: Play against a friend locally
- **GUI Interface**: Clean, intuitive 3×3 grid layout
- **Win Detection**: Automatically detects winners across all combinations
- **Draw Detection**: Identifies tie/draw situations
- **Winning Highlighting**: Highlights winning combination in green
- **Reset Button**: Easily start a new game
- **Player Indicator**: Shows whose turn it is

## Requirements

- Python 3.6+
- Tkinter (usually comes with Python)

## Installation & Setup

1. Navigate to the Tic Tac Toe folder:
```bash
cd "Tic Tac Toe"
```

2. Run the game:
```bash
python main.py
```

## How to Play

1. **Start Game**: Run `main.py` - the game board appears
2. **Game Rules**:
   - Player X goes first
   - Players take turns clicking empty squares
   - First to get 3 in a row (horizontal, vertical, or diagonal) wins
3. **Win Condition**: When someone wins, their squares turn green
4. **Draw Condition**: If all 9 squares are filled with no winner, it's a draw
5. **Reset**: Click "Reset Game" button to play again

## Winning Combinations

```
Row:     [0,1,2]  [3,4,5]  [6,7,8]
Col:     [0,3,6]  [1,4,7]  [2,5,8]
Diagonal: [0,4,8]  [2,4,6]
```

## Game Board Layout

```
 0 | 1 | 2
-----------
 3 | 4 | 5
-----------
 6 | 7 | 8
```

## Code Structure

```
main.py
├── check_winner()    → Detects winning combinations
├── check_draw()      → Detects draw/tie condition
├── button_click()    → Handles player moves
├── toggle_player()   → Switches between X and O
├── reset_game()      → Resets board for new game
└── GUI Setup         → Creates game board and UI
```

## Features Explained

| Feature | Description |
|---------|-------------|
| **Win Detection** | Checks all 8 winning combinations after each move |
| **Draw Detection** | When all 9 squares filled with no winner |
| **Button Disabling** | Buttons disabled after game ends |
| **Highlight Winner** | Winning squares turn green for clarity |
| **Player Turn Display** | Label shows whose turn it is |
| **Reset Button** | Start fresh game without closing app |

## Example Gameplay

```
Start: X's turn

Move 1 (X): Clicks center [4]
Move 2 (O): Clicks top-left [0]
Move 3 (X): Clicks bottom-right [8]
Move 4 (O): Clicks top-right [2]
Move 5 (X): Clicks top-center [1]
Result: X WINS! (diagonal: 0-4-8)
```

## Tips for Playing

- **Control Center**: Position [4] is strategically important
- **Strategy**: Block opponent while setting up your win
- **Pattern Recognition**: Look for opponent's winning moves

## Future Enhancements

- [ ] AI opponent (computer player)
- [ ] Difficulty levels for AI
- [ ] Score tracker across multiple games
- [ ] Game statistics (wins/losses/draws)
- [ ] Sound effects
- [ ] Different board themes and colors
- [ ] Network multiplayer

## Known Issues & Fixes

- **Case Inconsistency**: Make sure X and O are consistent (capital letters)
- **Button State**: Buttons are disabled after game ends correctly

## License

Open source - feel free to modify and extend!
